from ..markdown import Markdown, SchemeT
from ..nodes import Html
from ._types import Creator
from typing import Type


class Page:
    __slots__ = ("src", "out", "creator", "scheme")

    def __init__(
        self, src: str, out: str, creator: Creator, scheme: Type[SchemeT]
    ) -> None:
        self.src = src
        self.out = out
        self.creator = creator
        self.scheme = scheme

    def generate(self) -> Html:
        md = Markdown.load(path=self.src, scheme=self.scheme)
        return self.creator(str(md), **md.properties)
