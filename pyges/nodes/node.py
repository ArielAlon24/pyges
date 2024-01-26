from abc import ABC, abstractmethod
from typing import List, Union


class Node(ABC):
    __slots__ = tuple()

    @abstractmethod
    def __init__(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def dump(self, indent_size: int = 4, _rank: int = 0) -> str:
        raise NotImplementedError

    def __str__(self) -> str:
        return self.dump()


Value = Node | List[Union[Node, str]] | str | None
