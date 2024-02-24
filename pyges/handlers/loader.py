from .logger import Logger
from ..models import Config, Page, Asset
from ..nodes.markdown import Scheme
from typing import List, Type
from .._types import Creator
from pathlib import Path
from ..errors import LoadError
from enum import Enum


logger = Logger("Loader")


class Suffix(Enum):
    MARKDOWN = ".md"
    HTML = ".html"


class Loader:
    def __init__(self, config: Config) -> None:
        self.config = config
        logger.headline("Loading Pages")

    def load_style_sheet(self) -> Asset:
        logger.debug("Loading style sheet file")
        return self._create_asset(self.config.style_sheet)

    def load_assets(self) -> List[Asset]:
        logger.debug("Loading 'assets' folder")
        return [
            self._create_asset(path)
            for path in self.config.assets.rglob("*")
            if path.is_file()
        ]

    def load_cname(self) -> Asset:
        logger.debug("Loading 'CNAME' file")
        return self._create_asset(self.config.style_sheet)

    def load(self, path: str, creator: Creator, scheme: Type[Scheme]) -> List[Page]:
        path_from_root = Path(path)
        full_path = self.config.src / path_from_root

        if not full_path.exists():
            message = f"Cannot locate path '{path}' from creator '{creator.__name__}'"
            logger.error(message)
            raise LoadError(message)

        if full_path.is_file():
            return [self.load_page(path=path_from_root, creator=creator, scheme=scheme)]
        return self.load_pages(path=path_from_root, creator=creator, scheme=scheme)

    def load_page(self, path: Path, creator: Creator, scheme: Type[Scheme]) -> Page:
        if path.suffix != Suffix.MARKDOWN.value:
            message = "A single file creator must be a 'markdown' file"
            logger.error(message)
            raise LoadError(message)

        return self._create_page(path=path, creator=creator, scheme=scheme)

    def load_pages(
        self, path: Path, creator: Creator, scheme: Type[Scheme]
    ) -> List[Page]:
        logger.debug(f"Loading folder '{path}'")
        pages = []
        for sub_path in (self.config.src / path).iterdir():
            if sub_path.suffix != Suffix.MARKDOWN.value:
                message = f"Found a non markdown file - '{sub_path.relative_to(self.config.src)}' while traversing '{path}'."
                if not self.config.skip_non_markdown_files:
                    logger.error(message)
                    raise LoadError(message)
                else:
                    logger.warning(message)
                    continue
            pages.append(
                self._create_page(
                    path=sub_path.relative_to(self.config.src),
                    creator=creator,
                    scheme=scheme,
                )
            )
        return pages

    def _create_asset(self, path: Path) -> Asset:
        return Asset(
            src=path,
            path=path.relative_to(self.config.src),
        )

    def _create_page(self, path: Path, creator: Creator, scheme: Type[Scheme]) -> Page:
        logger.debug(f"Loading page '{path}'")
        return Page(
            src=self.config.src / path,
            path=path.with_suffix(Suffix.HTML.value),
            creator=creator,
            scheme=scheme,
        )


def read_bytes(path: Path) -> bytes:
    return path.read_bytes()
