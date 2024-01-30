from .typed_template import Template
from .config import Config


class Site:
    def __init__(self, config: Config) -> None:
        pass

    def generate(self, content: str, out: str) -> None:
        pass

    def add(self) -> None:
        pass
