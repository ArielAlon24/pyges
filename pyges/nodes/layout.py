from .tag import Tag
from .node import Value


class Html(Tag):
    DOCTYPE_TAG: str = "<!DOCTYPE html>"

    def __init__(
        self,
        value: Value = None,
        _class: str | None = None,
        _id: str | None = None,
        _style: str | None = None,
    ) -> None:
        super().__init__(value=value, _class=_class, _id=_id, _style=_style)

    def _dump(self, indent_size: int = 4, _rank: int = 0) -> str:
        return self.DOCTYPE_TAG + "\n" + super()._dump(indent_size, _rank)


class Body(Tag):
    def __init__(
        self,
        value: Value = None,
        _class: str | None = None,
        _id: str | None = None,
        _style: str | None = None,
    ) -> None:
        super().__init__(value=value, _class=_class, _id=_id, _style=_style)


class Head(Tag):
    def __init__(
        self,
        value: Value = None,
        _class: str | None = None,
        _id: str | None = None,
        _style: str | None = None,
    ) -> None:
        super().__init__(value=value, _class=_class, _id=_id, _style=_style)


class Title(Tag):
    def __init__(
        self,
        value: Value = None,
        _class: str | None = None,
        _id: str | None = None,
        _style: str | None = None,
        _self_closing: bool = False,
    ) -> None:
        super().__init__(value, _class, _id, _style, _self_closing)
