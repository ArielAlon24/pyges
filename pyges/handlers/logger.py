from colorama import init, Fore, Style, Back
from datetime import datetime
from enum import Enum
import shutil
from typing import Type

init(autoreset=True)


class Level(Enum):
    DEBUG = Fore.LIGHTBLUE_EX
    INFO = Fore.LIGHTCYAN_EX
    WARNING = Fore.YELLOW
    ERROR = Fore.RED


class Logger:
    FORMAT = (
        "{color}"
        + "{timestamp} {level: <10}"
        + Style.BRIGHT
        + "{name: <8}  "
        + Style.NORMAL
        + "{message}"
    )

    TIMESTAMP_FORMAT = "%H:%M:%S"
    HEADLINE_COLOR = Back.LIGHTBLUE_EX + Fore.BLACK + Style.BRIGHT

    def __init__(self, name: str) -> None:
        self.name = name

    def log(self, level: Level, message: str) -> None:
        timestamp = datetime.now().strftime(self.TIMESTAMP_FORMAT)
        print(
            self.FORMAT.format(
                color=level.value,
                level=f"[{level.name}]",
                timestamp=timestamp,
                name=self.name,
                message=message,
            )
        )

    def debug(self, message: str) -> None:
        self.log(level=Level.DEBUG, message=message)

    def info(self, message: str) -> None:
        self.log(level=Level.INFO, message=message)

    def warning(self, message: str) -> None:
        self.log(level=Level.WARNING, message=message)

    def error(self, message: str) -> None:
        self.log(level=Level.ERROR, message=message)

    def raise_error(self, message: str, factory: Type[Exception]) -> None:
        self.log(level=Level.ERROR, message=message)
        raise factory(message)

    def headline(self, message: str) -> None:
        width = shutil.get_terminal_size().columns
        padding = " " * ((width - len(message)) // 2)
        print(f"\n{self.HEADLINE_COLOR}{padding}{message}{padding}")
