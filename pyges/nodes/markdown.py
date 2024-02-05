from __future__ import annotations
from dataclasses import dataclass
import markdown as md
from markdown.extensions.codehilite import CodeHiliteExtension
from markdown.extensions.fenced_code import FencedCodeExtension
from typeguard import check_type, TypeCheckError
from typing import Type, Dict, Any, Tuple
import yaml
from pathlib import Path

from .node import Node


@dataclass
class Scheme:
    pass


class Markdown(Node):
    CODE_CLASS = "code"
    YAML_SEPARATOR = "---"

    def __init__(self, content: str) -> None:
        self.__content = content
        self.__html: str | None = None

    def dump(self, indent_size: int = 4, _rank: int = 0) -> str:
        return f"{_rank * indent_size * ' '}{self.html}"

    @property
    def html(self) -> str:
        if self.__html is None:
            self.__html = md.markdown(
                self.__content,
                extensions=[
                    FencedCodeExtension(),
                    CodeHiliteExtension(
                        linenums=True, use_pygments=True, css_class=Markdown.CODE_CLASS
                    ),
                ],
            )
        return self.__html

    @classmethod
    def load(
        cls, path: Path, scheme: Type[Scheme] = Scheme
    ) -> Tuple[Dict[str, Any], Markdown]:
        with path.open() as file:
            content = file.read()
        parts = content.split(Markdown.YAML_SEPARATOR)
        if len(parts) == 1:
            return {}, cls(content=content)
        elif len(parts) == 3:
            _, yaml_content, markdown_content = parts
            properties = yaml.safe_load(yaml_content)
            instance = cls(content=markdown_content)
            instance._validate(properties=properties, scheme=scheme)
            return properties, instance
        else:
            raise ValueError("Incorrect use of YAML separators.")

    @staticmethod
    def _validate(properties: Dict[str, Any], scheme: Type[Scheme]) -> None:
        if not hasattr(scheme, "__annotations__"):
            raise AttributeError("Scheme must have an '__annotations__' attribute.")
        annotations = scheme.__annotations__

        if len(annotations) != len(properties):
            raise ValueError("Keys count don't match scheme key count.")

        for key, expected_type in annotations.items():
            if key not in properties:
                raise KeyError(f"Missing key: '{key}' in properties.")
            try:
                check_type(properties[key], expected_type)
            except TypeCheckError as e:
                raise TypeError(f"Type mismatch for key '{key}': {e}")

    def __str__(self) -> str:
        return self.html

    def __repr__(self) -> str:
        return self.__content
