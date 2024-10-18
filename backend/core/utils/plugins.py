import importlib
import os
import logging
import sys


def load_plugins(plugins: list[str] | tuple[str], cat: str):
    logger = logging.getLogger("mundus")
    p_root = os.getenv("plugins").replace("$cwd", os.getcwd())

    if not isinstance(p_root, str):
        logger.error("plugins root not set!")
        return None

    if not os.path.exists(p_root):
        logger.error("plugins root not exist!")
        return

    logger.info(f"loading plugins @category='{cat}' from {p_root} ...")

    if p_root not in sys.path:
        sys.path.append(p_root)

    modules = []

    for plugin in plugins:
        module = importlib.import_module(plugin)

        # check if the module is valid
        if not hasattr(module, "Plugin"):
            logger.error(f"plugin '{plugin}' doesn't have class 'Plugin'")
            continue

        if not hasattr(module, "Parser"):
            logger.error(f"plugin '{plugin}' doesn't have class 'Parser'")
            continue

        if not hasattr(getattr(module, "Plugin", None), "start"):
            logger.error(f"plugin '{plugin}.Plugin' doesn't have class start function")
            continue

        logger.info(f"'{plugin}' loaded!")
        modules.append(module)

    return modules
