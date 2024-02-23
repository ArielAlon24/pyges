from .models import Config, Resource, Page
from typing import List, Collection
import shutil
from ._types import Creator


class Builder:
    def __init__(self, config: Config) -> None:
        self.config = config
        self.resources: List[Resource] = []

    def add(self, resources: Collection[Resource]) -> None:
        self.resources += resources

    def append(self, resource: Resource) -> None:
        self.resources.append(resource)

    def pages(self, creator: Creator) -> List[Page]:
        pages = []
        for resource in self.resources:
            if (
                isinstance(resource, Page)
                and resource.creator.__name__ == creator.__name__
            ):
                pages.append(resource)

        return pages

    def build(self) -> None:
        self.config.out.mkdir(exist_ok=True)
        self._clear_out()

        for resource in self.resources:
            path = self.config.out / resource.path
            data = resource.generate()
            path.parent.mkdir(parents=True, exist_ok=True)
            with path.open("wb") as file:
                file.write(data)

    def _clear_out(self) -> None:
        for item in self.config.out.iterdir():
            if item.is_dir():
                shutil.rmtree(item)
            else:
                item.unlink()
