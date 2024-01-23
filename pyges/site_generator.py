from .typed_template import Template


class SiteGenerator:
    def __init__(self) -> None:
        self.template = Template("a")
        pass

    def generate(self, content: str, out: str) -> None:
        pass
