from typing import List

from .node import Node, Value
from .string import String


class Tag(Node):
    def __init__(
        self,
        value: Value = None,
        _class: str | None = None,
        _id: str | None = None,
        _style: str | None = None,
        _self_closing: bool = False,
    ) -> None:
        self.nodes: List[Node] = []
        if not value:
            pass
        elif isinstance(value, Node):
            self.nodes.append(value)
        elif isinstance(value, str):
            self.nodes.append(String(value))
        else:
            for node in value:
                if isinstance(node, str):
                    self.nodes.append(String(node))
                else:
                    self.nodes.append(node)

        self._class = _class
        self._id = _id
        self._style = _style
        self.__self_closing = _self_closing

    def _name(self) -> str:
        return self.__class__.__name__.lower()

    def _attributes(self) -> List[str]:
        attributes = []

        if self._class:
            attributes.append(f'class="{self._class}"')

        if self._id:
            attributes.append(f'id="{self._id}"')

        if self._style:
            attributes.append(f'style="{self._style}"')

        return attributes

    def _dump(self, indent_size: int = 4, _rank: int = 0) -> str:
        name = self._name()
        _attributes = " ".join(self._attributes())
        attributes = f" {_attributes}" if _attributes else ""
        indent = " " * indent_size

        if self.__self_closing:
            return f"{indent * _rank}<{name}{attributes}/>"

        length = len(self.nodes)

        if not length:
            return f"{indent * _rank}<{name}{attributes}></{name}>"
        elif length == 1 and isinstance(self.nodes[0], String):
            return f"{indent * _rank}<{name}{attributes}> {self.nodes[0]._dump()} </{name}>"
        else:
            inner = "\n".join(
                tag._dump(indent_size, _rank=_rank + 1) for tag in self.nodes
            )
            return f"{indent * _rank}<{name}{attributes}>\n{inner}\n{indent * _rank}</{name}>"
