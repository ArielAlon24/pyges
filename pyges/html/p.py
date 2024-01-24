from .tag import Tag
from .html_node import HtmlNode
from typing import List


class P(Tag):
    def __init__(
        self,
        value: HtmlNode | List[HtmlNode] | None = None,
        _class: str | None = None,
        _id: str | None = None,
        _style: str | None = None,
    ) -> None:
        super().__init__(value=value, _class=_class, _id=_id, _style=_style)
