from abc import ABC, abstractmethod
from typing import List, Union


class Node(ABC):
    @abstractmethod
    def __init__(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def _dump(self, indent_size: int = 4, _rank: int = 0) -> str:
        raise NotImplementedError

    def __str__(self) -> str:
        return self._dump()


Value = Node | List[Union[Node, str]] | str | None
