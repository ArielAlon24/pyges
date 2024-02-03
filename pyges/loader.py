from .models import Config, Page, Asset
from .nodes.markdown import SchemeT
from typing import List, Type
from ._types import Creator
from pathlib import Path
from .errors import LoadError
from enum import Enum


class Suffix(Enum):
    MARKDOWN = ".md"
    HTML = ".html"


class Loader:
    def __init__(self, config: Config) -> None:
        self.config = config

    def load_style_sheet(self) -> Asset:
        return Asset(
            src=self.config.style_sheet,
            out=self.config.out / self.config.style_sheet.relative_to(self.config.src),
        )

    def load(self, path: str, creator: Creator, scheme: Type[SchemeT]) -> List[Page]:
        path_from_root = Path(path)
        full_path = self.config.src / path_from_root

        if not full_path.exists():
            raise LoadError(
                f"Path: {path} given by creator: {creator.__name__} was not found."
            )

        if not full_path.is_dir():
            return [
                self._create_page(path=path_from_root, creator=creator, scheme=scheme)
            ]

        pages = []
        for sub_path in full_path.iterdir():
            if sub_path.suffix != Suffix.MARKDOWN.value:
                if self.config.skip_non_markdown_files:
                    continue
                else:
                    raise LoadError(
                        f"Found non markdown file in {path} traversal for creator: {creator.__name__}."
                    )
            pages.append(
                self._create_page(
                    path=sub_path.relative_to(self.config.src),
                    creator=creator,
                    scheme=scheme,
                )
            )

        return pages

    def _create_page(self, path: Path, creator: Creator, scheme: Type[SchemeT]) -> Page:
        return Page(
            src=self.config.src / path,
            out=self.config.out / path.with_suffix(Suffix.HTML.value),
            creator=creator,
            scheme=scheme,
        )


def read_bytes(path: Path) -> bytes:
    return path.read_bytes()
