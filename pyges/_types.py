from typing import Callable

from .nodes import Markdown, Html

Creator = Callable[[Markdown], Html]
