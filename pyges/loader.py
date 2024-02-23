from .models import Config, Page, Asset
from .nodes.markdown import Scheme
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
            path=self.config.style_sheet.relative_to(self.config.src),
        )

    def load_assets(self) -> List[Asset]:
        return self._load_folder(self.config.assets)

    def load_cname(self) -> Asset:
        return Asset(
            src=self.config.cname,
            path=self.config.cname.relative_to(self.config.src),
        )

    def _load_folder(self, folder: Path) -> List[Asset]:
        assets = []
        for item in folder.rglob("*"):
            if item.is_file():
                path = item.relative_to(self.config.src)
                assets.append(Asset(src=item, path=path))
        return assets

    def load(self, path: str, creator: Creator, scheme: Type[Scheme]) -> List[Page]:
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

    def _create_page(self, path: Path, creator: Creator, scheme: Type[Scheme]) -> Page:
        return Page(
            src=self.config.src / path,
            path=path.with_suffix(Suffix.HTML.value),
            creator=creator,
            scheme=scheme,
        )


def read_bytes(path: Path) -> bytes:
    return path.read_bytes()
