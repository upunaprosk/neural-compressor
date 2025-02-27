# -*- coding: utf-8 -*-
# Copyright (c) 2023 Intel Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Main endpoint for GUI."""
import os
import time
from functools import wraps
from threading import Thread
from typing import Any, Callable

from flask import Blueprint, Flask
from flask import Request as WebRequest
from flask import jsonify, render_template, request
from flask_cors import CORS
from flask_socketio import SocketIO
from werkzeug.serving import make_ssl_devcert
from werkzeug.wrappers import Response as WebResponse

from neural_insights.components.workload_manager.workload_manager import WorkloadManager
from neural_insights.utils.consts import CONFIG_REFRESH_PERIOD
from neural_insights.utils.exceptions import InternalException
from neural_insights.utils.logger import log
from neural_insights.web.communication import MessageQueue, Request
from neural_insights.web.configuration import Configuration
from neural_insights.web.router import Router
from neural_insights.web.service.response_generator import ResponseGenerator

templates_dir = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "app",
    ),
)

app = Flask(
    __name__,
    static_folder=templates_dir,
    static_url_path="/",
    template_folder=templates_dir,
)
app_blueprint = Blueprint("Neural Insights", __name__)
socketio = SocketIO()

router = Router()

METHODS = ["GET", "POST"]

# Suppress TensorFlow messages
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

url_prefix: str = ""
workload_manager = None


def run_server(configuration: Configuration) -> None:
    """Run webserver on specified scheme, address and port."""
    addr = configuration.server_address
    server_port = configuration.server_port
    gui_port = configuration.gui_port
    token = configuration.token

    global url_prefix
    url_prefix = configuration.url_prefix

    cors_allowed_origins = f"{configuration.scheme}://{addr}:{gui_port}"

    app.config["JSON_SORT_KEYS"] = False
    app.register_blueprint(app_blueprint, url_prefix=url_prefix)
    app.secret_key = token
    CORS(app, origins=cors_allowed_origins)
    socketio.init_app(
        app,
        cors_allowed_origins=cors_allowed_origins,
        max_http_buffer_size=2000,
    )
    tls_args = get_tls_args(configuration)

    global workload_manager
    workload_manager = WorkloadManager(workdir_location=configuration.workdir)

    socketio.run(app, host=addr, port=server_port, **tls_args)


def get_tls_args(configuration: Configuration) -> dict:
    """Get TLS configuration."""
    if configuration.allow_insecure_connections:
        return {}

    if configuration.tls_certificate and configuration.tls_key:
        certfile = configuration.tls_certificate
        keyfile = configuration.tls_key
    else:
        os.makedirs(configuration.global_config_directory, mode=511, exist_ok=True)
        base_path = os.path.join(configuration.global_config_directory, "certificate")
        certfile = f"{base_path}.crt"
        keyfile = f"{base_path}.key"
        if not os.path.isfile(certfile) or not os.path.isfile(keyfile):
            certfile, keyfile = make_ssl_devcert(base_path)

    return {
        "certfile": certfile,
        "keyfile": keyfile,
        "do_handshake_on_connect": False,
    }


@app_blueprint.after_request
def block_iframe(response: WebResponse) -> WebResponse:
    """Block iframe and set others CSP."""
    response.headers["X-Frame-Options"] = "DENY"
    response.headers[
        "Content-Security-Policy"
    ] = "frame-ancestors 'none'; font-src 'self'; img-src 'self'; script-src 'self'"
    response.headers["Access-Control-Max-Age"] = "-1"
    return response


@app_blueprint.after_request
def block_sniffing(response: WebResponse) -> WebResponse:
    """Block MIME sniffing."""
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


def require_api_token(func: Callable) -> Any:
    """Validate authorization token."""

    @wraps(func)
    def check_token(*args: str, **kwargs: str) -> Any:
        """Validate that correct token was provided."""
        provided_token = request.headers.get(
            "Authorization",
            request.args.to_dict().get("token", None),
        )

        if not app.secret_key == provided_token:
            return (
                "Invalid token, please use the URL displayed by the server on startup",
                403,
            )

        return func(*args, **kwargs)

    return check_token


@app_blueprint.route("/", methods=METHODS)
def root() -> Any:
    """Serve JS application index."""
    return render_template("index.html", url_prefix=url_prefix)


@app_blueprint.route("/api/<path:subpath>", methods=METHODS)
@require_api_token
def handle_api_call(subpath: str) -> Any:
    """Handle API access."""
    try:
        parameters = build_parameters(subpath, request)
        response = router.handle(parameters)
        if isinstance(response, WebResponse):
            return response
        return jsonify(response.data)
    except Exception as err:
        if isinstance(err, InternalException):
            log.critical(err)
        return ResponseGenerator.from_exception(err)


@app_blueprint.route("/api/<path:subpath>", methods=["OPTIONS"])
def allow_api_call(subpath: str) -> Any:
    """Allow for API access."""
    return "OK"


@app.errorhandler(404)
def page_not_found(e: Any) -> Any:
    """Serve JS application index when no static file found."""
    return render_template(
        "index.html",
        url_prefix=url_prefix,
    )


@app_blueprint.after_request
def disable_cache(response: WebResponse) -> WebResponse:
    """Disable cache on all requests."""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    response.headers["Cache-Control"] = "public, max-age=0"
    return response


def build_parameters(endpoint: str, request: WebRequest) -> Request:
    """Build domain object from flask request."""
    data = request.get_json() if request.is_json else request.args.to_dict(flat=False)
    return Request(request.method, endpoint, data)


def web_socket_publisher(web_socket: SocketIO) -> None:
    """Send messages from queue via web-socket to GUI."""
    queue = MessageQueue()
    while True:
        message = queue.get()
        web_socket.emit(
            message.subject,
            {"status": message.status, "data": message.data},
        )
        socketio.sleep(0)


publisher = Thread(
    target=web_socket_publisher,
    args=(socketio,),
)
publisher.daemon = True
publisher.start()


def config_watcher(period_in_s: int) -> None:
    """Observe config for changes and send notification when changed."""
    queue = MessageQueue()
    config_modification_time = None
    if workload_manager is not None:
        config_modification_time = os.stat(workload_manager.config_path).st_mtime
    while True:
        time.sleep(period_in_s)
        if workload_manager is None:
            continue
        config_path = workload_manager.config_path
        config_mod_time_new = os.stat(config_path).st_mtime
        if config_modification_time != config_mod_time_new:
            config_modification_time = config_mod_time_new
            queue.post_info("Config update", "Workload config has been modified.")


conf_watcher = Thread(
    target=config_watcher,
    args=(CONFIG_REFRESH_PERIOD,),
)
conf_watcher.daemon = True
conf_watcher.start()
