from flask import Flask


app = Flask(__name__)


def supress_flask_logs() -> None:
    import logging

    wsgi_logger = logging.getLogger("werkzeug")
    wsgi_logger.setLevel(logging.ERROR)

    import click

    def silent(*_) -> None:
        pass

    click.echo = silent
    click.secho = silent


@app.route("/")
def index() -> str:
    return "test"


@app.route("/test")
def test() -> str:
    return "what!!"


if __name__ == "__main__":
    supress_flask_logs()
    app.run(host="localhost", port=5000, debug=True)
