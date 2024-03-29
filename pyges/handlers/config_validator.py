from ..models import Config
from .logger import Logger
from ..errors import ConfigError

logger = Logger(__name__)


def validate_config(config: Config) -> None:
    logger.headline("Validating Config")

    # src
    if not config.src.is_dir():
        logger.raise_error(
            f"Cannot locate 'src' folder, '{config.src}' does not exist or is not a directory",
            factory=ConfigError,
        )
    logger.debug(f"Found 'src' folder: '{config.src}'")

    # out
    logger.debug(f"Set 'out' folder: '{config.out}'")

    # style_sheet
    if not config.style_sheet.exists():
        logger.raise_error(
            f"Cannot locate style sheet at '/{config.style_sheet.relative_to(config.src)}'.",
            factory=ConfigError,
        )
    logger.debug(
        f"Found style sheet file: '/{config.style_sheet.relative_to(config.src)}'"
    )

    # assets
    if not config.assets.is_dir():
        logger.raise_error(
            f"Cannot loacte assets folder at '/{config.assets.relative_to(config.src)}'",
            factory=ConfigError,
        )
    logger.debug(f"Found 'assets' folder: '/{config.assets.relative_to(config.src)}'")

    # cname
    if not config.cname.exists():
        logger.raise_error(
            f"Cannot loacte CNAME file at '/{config.cname.relative_to(config.src)}'",
            factory=ConfigError,
        )
    logger.debug(f"Found 'CNAME' file: '/{config.cname.relative_to(config.src)}'")
