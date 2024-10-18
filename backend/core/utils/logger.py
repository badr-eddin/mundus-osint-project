import logging
import os

from colorama import Fore


class CustomFormatter(logging.Formatter):
    def __init__(self, fmt=None):
        super().__init__(fmt)
        fmt = fmt or "<%(filename)s:%(lineno)s> %(message)s"

        self.formats = {
            logging.DEBUG: Fore.LIGHTWHITE_EX + fmt + Fore.RESET,
            logging.INFO: Fore.RESET + fmt + Fore.RESET,
            logging.WARN: Fore.LIGHTYELLOW_EX + fmt + Fore.RESET,
            logging.ERROR: Fore.LIGHTRED_EX + fmt + Fore.RESET,
            logging.CRITICAL: Fore.RED + fmt + Fore.RESET,
        }

    def format(self, record):
        log_fmt = self.formats.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


def get_logger(name=os.getenv("root_logger_name")) -> logging.Logger:
    logger = logging.getLogger(name)
    handler = logging.StreamHandler()
    handler.setFormatter(CustomFormatter())
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)

    return logger
