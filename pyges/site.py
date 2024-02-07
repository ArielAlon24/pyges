from typing import Callable, Type, List
from .nodes import Html
from .nodes.markdown import Scheme
from ._types import Creator
from .models import Config, Page
from .builder import Builder
from .loader import Loader


class Site:
    def __init__(self, config: Config) -> None:
        self.loader = Loader(config=config)
        self.builder = Builder(config=config)
        self._setup()

    def _setup(self) -> None:
        self.builder.append(self.loader.load_style_sheet())
        self.builder.add(self.loader.load_assets())
        self.builder.append(self.loader.load_cname())

    def build(self) -> None:
        self.builder.build()

    def pages(self, creator: Creator) -> List[Page]:
        return self.builder.pages(creator)

    def add(self, path: str, scheme: Type[Scheme] = Scheme) -> Callable[..., Creator]:
        def decorator(creator: Creator) -> Creator:
            def wrapper(*args, **kwargs) -> Html:
                return creator(*args, **kwargs)

            pages = self.loader.load(path=path, creator=creator, scheme=scheme)
            self.builder.add(pages)
            wrapper.__name__ = creator.__name__
            return wrapper

        return decorator
