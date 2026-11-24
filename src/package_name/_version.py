from importlib.metadata import version

PACKAGE_NAME = "package_name"

try:
    __version__ = version(PACKAGE_NAME)
except Exception:
    __version__ = "0.0.0-dev"


APP_NAME = f"{PACKAGE_NAME.replace('_', ' ').capitalize()} - {__version__}"
