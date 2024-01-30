import markdown as md  # Avoiding confusion with this module name.
from markdown.extensions.fenced_code import FencedCodeExtension
from markdown.extensions.codehilite import CodeHiliteExtension
import os


class Markdown:
    def __init__(self, content: str) -> None:
        self.content = content

    def __str__(self) -> str:
        return md.markdown(
            self.content,
            extensions=[
                FencedCodeExtension(),
                CodeHiliteExtension(linenums=True, use_pygments=True, css_class="code"),
            ],
        )

    def __repr__(self) -> str:
        return self.content


class MarkdownFile(Markdown):
    def __init__(self, path: str) -> None:
        if not os.path.exists(path):
            raise FileNotFoundError(f"Couldn't find '{path}'.")
        with open(path) as file:
            content = file.read()
        super().__init__(content)
