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


Attributes = Dict[Attribute, str]
