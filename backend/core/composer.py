"""
OUTPUT STRUCTURE

{
    "website-url": [A1s, ....] || {A1}
}

A1
{
    "field": "value"
}
"""

import pathlib
import dotenv
from . import utils
from .utils import plugins, logger, config


class mundus:
    def __init__(self):
        self.logger = logger.get_logger()

        self.logger.info("starting program ...")
        self.load_env_vars()

        self.config = config.read("/")

    def load_env_vars(self):
        self.logger.info("loading environment variables ...")
        path = pathlib.Path(__file__).parent.as_posix()
        dotenv.load_dotenv(f"{path}/config/.env", verbose=True)

    # general information gathering
    def track_person_by_name(self, **kwargs):
        self.logger.info("tracking person by name ...")

        if not (self.config.get("plugins") or {}).get("names"):
            self.logger.error("no plugins were found! if otherwise check 'data/config.toml' file.")
            return

        loaded_plugins = plugins.load_plugins(self.config["plugins"]["names"], "names")

        information = []

        for plugin in loaded_plugins:
            try:
                class_ = getattr(plugin, "Plugin", None)
                if not class_:
                    self.logger.error("entry class not implemented!")
                    continue

                class_ = class_(utils=utils, **kwargs)
                output = class_.start()

                if not isinstance(output, (dict, list)):
                    self.logger.warning(f"plugin '{class_}' has unexpected output type!")
                    continue

                information.append(output)

            except Exception as e:
                self.logger.error(e)

    def track_phone_number(self):
        pass

    def track_username(self):
        pass

    # specific information gathering

