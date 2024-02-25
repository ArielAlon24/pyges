from typing import Callable, Type, List
import sys
import time

from .errors import BuildError, LoadError, ConfigError
from .nodes import Html, Scheme
from ._types import Creator
from .models import Config, Page
from .handlers import Loader, Builder, Logger, validate_config, Runtime

logger = Logger(__name__)


class Site:
    def __init__(self, config: Config) -> None:
        try:
            validate_config(config)
        except ConfigError:
            sys.exit(1)

        self.loader = Loader(config=config)
        self.builder = Builder(config=config)
        self.config = config
        self._setup()

    def _setup(self) -> None:
        self.builder.append(self.loader.load_style_sheet())
        self.builder.add(self.loader.load_assets())
        self.builder.append(self.loader.load_cname())

    def build(self) -> None:
        start = time.perf_counter()
        try:
            self.builder.build()
        except BuildError:
            sys.exit(1)

        end = time.perf_counter()
        logger.headline(
            f"Build Completed. Took {end - start:.3f} secs", theme=Logger.CYAN_HEADLINE
        )

    def debug(self) -> None:
        runtime = Runtime(builder=self.builder, config=self.config)
        try:
            runtime.run()
        except RuntimeError:
            sys.exit(1)

    def pages(self, creator: Creator) -> List[Page]:
        return self.builder.pages(creator)

    def add(self, path: str, scheme: Type[Scheme] = Scheme) -> Callable[..., Creator]:
        def decorator(creator: Creator) -> Creator:
            def wrapper(*args, **kwargs) -> Html:
                return creator(*args, **kwargs)

            try:
                pages = self.loader.load(path=path, creator=creator, scheme=scheme)
            except LoadError:
                sys.exit(1)
            self.builder.add(pages)
            wrapper.__name__ = creator.__name__
            return wrapper

        return decorator
