from typing import Callable, List, Type

from .nodes import Html
from .markdown import Scheme, SchemeT
from ._types import Creator
from .models import Config, Page, BuildError

import os
import shutil


class Site:
    def __init__(self, config: Config) -> None:
        self.pages: List[Page] = []
        self.config = config

    def build(self) -> None:
        try:
            self._build()
        except BuildError:
            # log
            if os.path.exists(self.config.out):
                shutil.rmtree(self.config.out)

    def _build(self) -> None:
        if os.path.exists(self.config.out):
            shutil.rmtree(self.config.out)

        os.mkdir(self.config.out)

        if not os.path.exists(self.config.out):
            raise BuildError(f"Couldn't create out folder: {self.config.out}")

        for page in self.pages:
            html = page.generate()

            with open(page.out, "w") as file:
                file.write(str(html))

    def add(self, path: str, scheme: Type[SchemeT] = Scheme) -> Callable[..., Creator]:
        def decorator(creator: Creator) -> Creator:
            def wrapper(*args, **kwargs) -> Html:
                return creator(*args, **kwargs)

            self.pages.append(
                Page(
                    src=self.config.src + path,
                    out=self.config.out + path.removesuffix("md") + "html",
                    creator=creator,
                    scheme=scheme,
                )
            )
            return wrapper

        return decorator
