from typing import List

from .node import Node, Value
from .string import String
from .attributes import Attributes


class Tag(Node):
    __slots__ = ("nodes", "attributes")
    __is_void__ = False

    def __init__(
        self,
        value: Value | None = None,
        attributes: Attributes | None = None,
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

        if not attributes:
            self.attributes = {}
        else:
            self.attributes = attributes

    @property
    def name(self) -> str:
        return self.__class__.__name__.lower()

    def _format_attributes(self) -> str:
        result = ""
        for attribute, value in self.attributes.items():
            result += f' {attribute.name.lower()}="{value}"'

        return result

    def dump(self, indent_size: int = 4, _rank: int = 0) -> str:
        attributes = self._format_attributes()
        indent = " " * indent_size

        if self.__is_void__:
            return f"{indent * _rank}<{self.name}{attributes}>"

        length = len(self.nodes)

        if not length:
            return f"{indent * _rank}<{self.name}{attributes}></{self.name}>"
        elif length == 1 and isinstance(self.nodes[0], String):
            return f"{indent * _rank}<{self.name}{attributes}> {self.nodes[0].dump()} </{self.name}>"
        else:
            inner = "\n".join(
                tag.dump(indent_size, _rank=_rank + 1) for tag in self.nodes
            )
            return f"{indent * _rank}<{self.name}{attributes}>\n{inner}\n{indent * _rank}</{self.name}>"
