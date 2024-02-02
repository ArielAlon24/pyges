from __future__ import annotations

import markdown as md  # Avoiding confusion with this module name.
from markdown.extensions.codehilite import CodeHiliteExtension
from markdown.extensions.fenced_code import FencedCodeExtension
from typeguard import check_type, TypeCheckError
from typing import Type, Dict, Any
import yaml
import os
from .scheme import Scheme, SchemeT


class Markdown:
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
    def load(cls, path: str, scheme: Type[SchemeT]) -> Markdown:
        if not os.path.exists(path):
            raise FileNotFoundError(f"Couldn't find '{path}'.")
        with open(path) as file:
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
