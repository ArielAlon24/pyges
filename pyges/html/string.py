from .html_node import HtmlNode


class String(HtmlNode):
    def __init__(self, string: str) -> None:
        self.string = string

    def _dump(self, indent_size: int = 4, _rank: int = 0) -> str:
        return f"{_rank * indent_size * ' '}{self.string}"
