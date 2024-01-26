from .tag import Tag
from .node import Value
from .attributes import Attribute
from typing import Dict


class H(Tag):
    def __init__(
        self,
        size: int,
        value: Value = None,
        attributes: Dict[Attribute, str] | None = None,
    ) -> None:
        super().__init__(value=value, attributes=attributes)
        if size < 0 or size > 6:
            raise ValueError("H tag must have a size value between 1 - 6.")
        self.size = size

    @property
    def name(self) -> str:
        return super().name + str(self.size)


class Br(Tag):
    __is_void__ = True


class P(Tag):
    pass


class Span(Tag):
    pass


class B(Tag):
    pass


class I(Tag):
    pass


class Strong(Tag):
    pass


class Em(Tag):
    pass


class Mark(Tag):
    pass


class Small(Tag):
    pass


class Del(Tag):
    pass


class Ins(Tag):
    pass


class Sub(Tag):
    pass


class Sup(Tag):
    pass
