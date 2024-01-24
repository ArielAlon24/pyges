from .tag import Tag
from .node import Value


class H(Tag):
    def __init__(
        self,
        size: int,
        value: Value = None,
        _class: str | None = None,
        _id: str | None = None,
        _style: str | None = None,
    ) -> None:
        super().__init__(value=value, _class=_class, _id=_id, _style=_style)
        if size < 0 or size > 6:
            raise ValueError("H tag must have a size value between 1 - 6.")
        self.size = size

    def _name(self) -> str:
        return super()._name() + str(self.size)


class P(Tag):
    def __init__(
        self,
        value: Value = None,
        _class: str | None = None,
        _id: str | None = None,
        _style: str | None = None,
    ) -> None:
        super().__init__(value=value, _class=_class, _id=_id, _style=_style)


class Span(Tag):
    def __init__(
        self,
        value: Value = None,
        _class: str | None = None,
        _id: str | None = None,
        _style: str | None = None,
    ) -> None:
        super().__init__(value=value, _class=_class, _id=_id, _style=_style)


class Br(Tag):
    def __init__(
        self,
        _class: str | None = None,
        _id: str | None = None,
        _style: str | None = None,
    ) -> None:
        super().__init__(_class=_class, _id=_id, _style=_style, _self_closing=True)


class B(Tag):
    def __init__(
        self,
        value: Value = None,
        _class: str | None = None,
        _id: str | None = None,
        _style: str | None = None,
        _self_closing: bool = False,
    ) -> None:
        super().__init__(value, _class, _id, _style, _self_closing)


class I(Tag):
    def __init__(
        self,
        value: Value = None,
        _class: str | None = None,
        _id: str | None = None,
        _style: str | None = None,
        _self_closing: bool = False,
    ) -> None:
        super().__init__(value, _class, _id, _style, _self_closing)


class Strong(Tag):
    def __init__(
        self,
        value: Value = None,
        _class: str | None = None,
        _id: str | None = None,
        _style: str | None = None,
        _self_closing: bool = False,
    ) -> None:
        super().__init__(value, _class, _id, _style, _self_closing)


class Em(Tag):
    def __init__(
        self,
        value: Value = None,
        _class: str | None = None,
        _id: str | None = None,
        _style: str | None = None,
        _self_closing: bool = False,
    ) -> None:
        super().__init__(value, _class, _id, _style, _self_closing)


class Mark(Tag):
    def __init__(
        self,
        value: Value = None,
        _class: str | None = None,
        _id: str | None = None,
        _style: str | None = None,
        _self_closing: bool = False,
    ) -> None:
        super().__init__(value, _class, _id, _style, _self_closing)


class Small(Tag):
    def __init__(
        self,
        value: Value = None,
        _class: str | None = None,
        _id: str | None = None,
        _style: str | None = None,
        _self_closing: bool = False,
    ) -> None:
        super().__init__(value, _class, _id, _style, _self_closing)
