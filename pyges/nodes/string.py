from .node import Node
import html


class String(Node):
    def __init__(self, string: str) -> None:
        self.string = string

    def dump(self, indent_size: int = 4, _rank: int = 0) -> str:
        return f"{_rank * indent_size * ' '}{html.escape(self.string)}"
