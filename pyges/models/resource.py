from ..nodes.markdown import Markdown, Scheme
from .._types import Creator
from typing import Type
from pathlib import Path
from abc import ABC, abstractmethod


class Resource(ABC):
    __slots__ = ("src", "path")

    def __init__(self, src: Path, path: Path) -> None:
        self.src = src
        self.path = path

    @abstractmethod
    def generate(self) -> bytes:
        raise NotImplementedError


class Page(Resource):
    __slots__ = ("creator", "content", "properties")

    def __init__(
        self, src: Path, path: Path, creator: Creator, scheme: Type[Scheme]
    ) -> None:
        super().__init__(src=src, path=path)
        self.creator = creator
        properties, md = Markdown.load(path=self.src, scheme=scheme)
        self.content = md
        self.properties = properties

    def generate(self) -> bytes:
        return bytes(self.creator(self.content, **self.properties))


class Asset(Resource):
    def generate(self) -> bytes:
        return self.src.read_bytes()
