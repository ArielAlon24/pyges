from .tag import Tag


class Html(Tag):
    DOCTYPE_TAG: str = "<!DOCTYPE html>"

    def dump(self, indent_size: int = 4, _rank: int = 0) -> str:
        return self.DOCTYPE_TAG + "\n" + super().dump(indent_size, _rank)


class Body(Tag):
    pass


class Head(Tag):
    pass


class Title(Tag):
    __self_closing = True
