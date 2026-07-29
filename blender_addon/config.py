from pathlib import Path

from .constants import CONFIG_FILENAME


class ConfigManager:

    def __init__(self):

        self.project_folder = Path.home()

        self.bridge_folder = ""

        self.auto_import = True

        self.auto_clean = False

    @property
    def config_path(self):

        return self.project_folder / CONFIG_FILENAME


config = ConfigManager()