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

    @abstractmethod
    def __repr__(self) -> str:
        raise NotImplementedError


class Page(Resource):
    __slots__ = ("creator", "scheme", "properties", "content")

    def __init__(
        self, src: Path, path: Path, creator: Creator, scheme: Type[Scheme]
    ) -> None:
        super().__init__(src=src, path=path)
        self.creator = creator
        self.scheme = scheme
        properties, content = Markdown.load(path=self.src, scheme=self.scheme)
        self.properties = properties
        self.content = content

    def generate(self) -> bytes:
        self.properties, self.content = Markdown.load(path=self.src, scheme=self.scheme)
        return bytes(self.creator(self.content, **self.properties))

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(path={self.path}, creator={self.creator.__name__})"


class Asset(Resource):
    def generate(self) -> bytes:
        return self.src.read_bytes()

    def update(self) -> None:
        pass

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(path={self.path})"
