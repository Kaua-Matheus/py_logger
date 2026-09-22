import datetime
from enum import Enum


# Public

class LogLevel(str, Enum):

    OK = "ok"
    INFO = "info"
    ERROR = "err"
    WARNING = "warn"


# Private

class _Color(str, Enum):

    GREEN = "\033[1;32m"
    BLUE = "\033[1;34m"
    RED = "\033[1;31m"
    YELLOW = "\033[1;33m"
    RESET = "\033[0m"

_STYLES = {
    LogLevel.OK: ("OK", _Color.GREEN),
    LogLevel.WARNING: ("WARNING", _Color.YELLOW),
    LogLevel.ERROR: ("ERROR", _Color.RED),
    LogLevel.INFO: ("INFO", _Color.BLUE)
}


class Logger():

    """
    Wrap text in a format ideal for debugging.
    """

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
            

    def __wrapper(self, text: str, code: str) -> str:
        return f"{code}{text}{_Color.RESET.value}"

    def log(self, text: str, level: str = "info", detail: bool = False) -> str:
        """
        Show text with a color and label depending on level

        Avaliable options (str):
            - "info" (default option)
            - "ok"
            - "err"
            - "warn"

        Parameters:
        text (str): The text that will be wrapped.
        level (str): The enum value from "LogLevel" that chose the style of logging.
        detail (bool): If true insert timestamp for a log.

        Return:
        str: Final wrapped text.
        """

        try:

            label, color = _STYLES.get(LogLevel(level), _STYLES[LogLevel.INFO])
            tag = self.__wrapper(label, color.value)

            if detail:
                ts = self.__wrapper(datetime.datetime.now().strftime("%H:%M:%S"), color.value)
                line = "[{} - {}]: {}".format(tag, ts, text)
            else:
                line = "[{}]: {}".format(tag, text)

            print(line)
            return line

        except Exception as e:
            raise e