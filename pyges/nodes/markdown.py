from __future__ import annotations

import markdown as md  # Avoiding confusion with this module name.
from markdown.extensions.codehilite import CodeHiliteExtension
from markdown.extensions.fenced_code import FencedCodeExtension
from typeguard import check_type, TypeCheckError
from typing import Type, Dict, Any
import yaml

from .string import String
from pathlib import Path

from typing import TypeVar


class Scheme:
    pass


SchemeT = TypeVar("SchemeT", bound=Scheme)


class Markdown(String):
    CODE_CLASS = "code"
    YAML_SEPERATOR = "---"

    def __init__(self, content: str, scheme: Type[SchemeT] = Scheme) -> None:
        parts = content.split(Markdown.YAML_SEPERATOR)
        self.properties = {}
        if len(parts) == 1:
            self.__content = content
        elif len(parts) == 3:
            if scheme is None:
                raise ValueError("A markdown with yaml must provide a yaml scheme.")
            _, _yaml, _markdown = parts
            properties = yaml.safe_load(_yaml)
            self._validate(properties=properties, scheme=scheme)
            self.properties |= properties
            self.__content = _markdown
        else:
            raise ValueError("Inccorect use of yaml seperators.")
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
    def load(cls, path: Path, scheme: Type[SchemeT]) -> Markdown:
        with path.open() as file:
            content = file.read()
        return cls(content=content, scheme=scheme)

    @staticmethod
    def _validate(properties: Dict[str, Any], scheme: Type[SchemeT]) -> None:
        if not hasattr(scheme, "__annotations__"):
            raise AttributeError("scheme must have an '__annotations__' attribute.")
        annotations = scheme.__annotations__

        if len(annotations) != len(properties):
            raise ValueError("Keys count don't match scheme key count.")

        for key, value in properties.items():
            try:
                check_type(value, annotations[key])
            except TypeCheckError:
                raise TypeError(
                    f"type mismatch for key '{key}', expected: {annotations[key]}"
                )
            except KeyError:
                raise KeyError(f"Unexpected key: '{key}'.")

    def __str__(self) -> str:
        return self.html

    def __repr__(self) -> str:
        return self.__content
