from enum import Enum
from typing import Dict


class Attribute(Enum):
    CLASS = "class"
    STYLE = "style"
    ID = "id"

    SRC = "src"
    ALT = "alt"

    REL = "rel"
    HREF = "href"
    TYPE = "type"

    NAME = "name"
    CONTENT = "content"


class DataAttribute:
    def __init__(self, name: str) -> None:
        self.__name = name.lower()

    @property
    def name(self) -> str:
        return f"data-{self.__name}"


Attributes = Dict[Attribute | DataAttribute, str]
