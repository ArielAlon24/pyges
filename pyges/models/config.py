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
    ) -> None:
        self.src = Path(src).resolve()
        if not self.src.is_dir():
            raise ValueError(
                f"src path '{self.src}' does not exist or is not a directory."
            )

        self.out = Path(out if out else self.DEFAULT_OUT).resolve()

        self.style_sheet = self.src / Path(
            style_sheet if style_sheet else self.DEFAULT_STYLES
        )
        if not self.style_sheet.exists():
            raise ValueError(f"stylessheet path '{self.src}' does not exist.")

        self.assets = self.src / Path(assets if assets else self.DEFAULT_ASSETS)
        if not self.assets.is_dir():
            raise ValueError(
                f"stylessheet path '{self.src}' does not exist or not a directory."
            )

        self.cname = self.src / Path(cname if cname else self.DEFAULT_CNAME)
        if not self.cname.exists():
            raise ValueError(f"CNAME path '{self.src}' does not exist.")

        self.skip_non_markdown_files = skip_non_markdown_files
