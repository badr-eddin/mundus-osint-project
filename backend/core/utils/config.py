import logging

import dpath.util as dutil
import toml
import pathlib
import os


def read(path, default="", sep="/"):
    logger = logging.getLogger(os.getenv("root_logger_name"))
    cfg_path = pathlib.Path(__file__).parent.parent.as_posix()
    cfg_path = os.path.join(cfg_path, "config", "config.toml")

    if not os.path.exists(cfg_path):
        logger.error("config file not found!")
        return default

    if os.path.isdir(cfg_path):
        logger.error("config 'file' is directory!")
        return default

    config = toml.loads(open(cfg_path).read())

    return dutil.get(config, path, sep, default)
