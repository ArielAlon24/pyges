from .tag import Tag
from .html_node import HtmlNode
from typing import List


class H(Tag):
    def __init__(
        self,
        size: int,
        _class: str | None = None,
        _id: str | None = None,
        _style: str | None = None,
        value: HtmlNode | List[HtmlNode] | None = None,
    ) -> None:
        super().__init__(value=value, _class=_class, _id=_id, _style=_style)
        self.size = size

    def _name(self) -> str:
        return super()._name() + str(self.size)
