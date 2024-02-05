from typing import Callable

from .nodes import Markdown
from pyges.nodes import Html

Creator = Callable[[Markdown], Html]
