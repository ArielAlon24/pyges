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


Attributes = Dict[Attribute, str]
