from .tag import Tag
from .node import Value


class Div(Tag):
    def __init__(
        self,
        value: Value = None,
        _class: str | None = None,
        _id: str | None = None,
        _style: str | None = None,
    ) -> None:
        super().__init__(value=value, _class=_class, _id=_id, _style=_style)
