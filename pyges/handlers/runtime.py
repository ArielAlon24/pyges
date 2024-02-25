from typing import Callable
from .builder import Builder
from .logger import Logger
from ..models import Config, Resource
from flask import Flask, request, Response
from pathlib import Path

logger = Logger("Runtime")


class Runtime:
    WSGI = "werkzeug"

    def __init__(self, builder: Builder, config: Config) -> None:
        self.builder = builder
        self.config = config
        self.app = Flask(self.__class__.__name__)
        self.app.before_request(self._before_request)
        self.app.after_request(self._after_request)
        self.app.teardown_request(self._teardown_request)
        self._suppress_flask_logging()

    def _suppress_flask_logging(self) -> None:
        import logging

        wsgi_logger = logging.getLogger(self.WSGI)
        wsgi_logger.setLevel(logging.ERROR)

        import click

        def silent(*_) -> None:
            pass

        click.echo = silent
        click.secho = silent

    def _before_request(self) -> None:
        if request.method != "GET":
            logger.warning(
                f"Recieved a non GET request - [{request.method} {request.path}]"
            )

    def _after_request(self, response: Response) -> Response:
        if response.status_code != 200:
            logger.warning(
                f"[{request.method} {request.path}] -> {response.status_code}"
            )
        else:
            logger.info(f"[{request.method} {request.path}] -> {response.status_code}")
        return response

    def _teardown_request(self, exception: Exception | None = None) -> None:
        if exception:
            logger.error(
                f"An exception occured in [{request.method} {request.path}]: {repr(exception)}"
            )

    def run(self) -> None:
        logger.headline(f"Routing Resources")
        total = len(self.builder.resources)
        logger.debug(f"Runtime is loaded with {total} resources")

        for index, resource in enumerate(self.builder.resources):
            path = self._create_url(resource.path)
            logger.debug(f"({index + 1}/{total}) Routing {path}")
            self.app.route(path)(self._create_view_function(resource))

        try:
            self._run()
        except Exception as e:
            logger.raise_error(str(e), RuntimeError)

    @staticmethod
    def _create_url(path: Path) -> str:
        *parts, file = path.parts
        if file == "index.html":
            return "/" + "/".join(parts)
        return "/" + str(path)

    @staticmethod
    def _create_view_function(resource: Resource) -> Callable[[], bytes]:
        def f():
            return resource.generate()

        f.__name__ = repr(resource.src)
        return f

    def _run(self) -> None:
        logger.headline(
            f"Runtime",
            theme=Logger.CYAN_HEADLINE,
        )
        self.app.run(host="localhost", port=self.config.debug_port)
