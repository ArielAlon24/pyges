from pathlib import Path


class Config:
    DEFAULT_OUT = "out"
    DEFAULT_STYLES = "styles.css"
    DEFAULT_ASSETS = "assets"
    DEFAULT_CNAME = "CNAME"

    def __init__(
        self,
        src: str,
        out: str | None = None,
        style_sheet: str | None = None,
        assets: str | None = None,
        cname: str | None = None,
        skip_non_markdown_files: bool = False,
        debug_port: int = 5000,
    ) -> None:
        self.src = Path(src).resolve()
        self.out = Path(out if out else self.DEFAULT_OUT).resolve()
        self.style_sheet = self.src / Path(
            style_sheet if style_sheet else self.DEFAULT_STYLES
        )
        self.assets = self.src / Path(assets if assets else self.DEFAULT_ASSETS)
        self.cname = self.src / Path(cname if cname else self.DEFAULT_CNAME)
        self.skip_non_markdown_files = skip_non_markdown_files
        self.debug_port = debug_port
