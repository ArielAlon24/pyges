from .node import Value
from .tag import Tag
from typing import List


class Img(Tag):
    def __init__(
        self,
        src: str,
        value: Value = None,
        _alt: str | None = None,
        _class: str | None = None,
        _id: str | None = None,
        _style: str | None = None,
    ) -> None:
        super().__init__(
            value=value, _class=_class, _id=_id, _style=_style, _self_closing=True
        )
        self.src = src
        self._alt = _alt

    def _attributes(self) -> List[str]:
        attributes = super()._attributes()

        attributes.append(f'src="{self.src}"')
        if self._alt:
            attributes.append(f'alt="{self._alt}"')

        return attributes
