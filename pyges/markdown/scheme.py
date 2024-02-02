from typing import TypeVar


class Scheme:
    pass


SchemeT = TypeVar("SchemeT", bound=Scheme)
