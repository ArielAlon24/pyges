from ..nodes.markdown import Markdown, SchemeT
from .._types import Creator
from typing import Type
from pathlib import Path
from abc import ABC, abstractmethod


class Resource(ABC):
    __slots__ = ("src", "out")

    def __init__(self, src: Path, out: Path) -> None:
        self.src = src
        self.out = out

    @abstractmethod
    def generate(self) -> bytes:
        raise NotImplementedError


class Page(Resource):
    __slots__ = ("creator", "scheme")

    def __init__(
        self, src: Path, out: Path, creator: Creator, scheme: Type[SchemeT]
    ) -> None:
        super().__init__(src=src, out=out)
        self.creator = creator
        self.scheme = scheme

    def generate(self) -> bytes:
        md = Markdown.load(path=self.src, scheme=self.scheme)
        return bytes(self.creator(md, **md.properties))


class Asset(Resource):
    def generate(self) -> bytes:
        return self.src.read_bytes()
