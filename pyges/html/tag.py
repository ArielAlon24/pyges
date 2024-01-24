from typing import List

from .html_node import HtmlNode
from .string import String


class Tag(HtmlNode):
    def __init__(
        self,
        value: HtmlNode | List[HtmlNode] | None = None,
        _class: str | None = None,
        _id: str | None = None,
        _style: str | None = None,
        __self_closing: bool = False,
    ) -> None:
        self.tags: List[HtmlNode]
        if not value:
            self.tags = []
        elif isinstance(value, HtmlNode):
            self.tags = [value]
        else:
            self.tags = value

        self._class = _class
        self._id = _id
        self._style = _style
        self.__self_closing = __self_closing

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
            return f"{indent * _rank}<{name} {attributes}/>"

        length = len(self.tags)

        if not length:
            return f"{indent * _rank}<{name}{attributes}></{name}>"
        elif length == 1 and isinstance(self.tags[0], String):
            return (
                f"{indent * _rank}<{name}{attributes}> {self.tags[0]._dump()} </{name}>"
            )
        else:
            inner = "\n".join(
                tag._dump(indent_size, _rank=_rank + 1) for tag in self.tags
            )
            return f"{indent * _rank}<{name}{attributes}>\n{inner}\n{indent * _rank}</{name}>"
