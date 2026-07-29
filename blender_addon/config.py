from pathlib import Path

from .constants import CONFIG_FILENAME


class Config:

    def __init__(self):

        self.root = Path.home()

        self.bridge_folder = ""

    @property
    def config_path(self):

        return self.root / CONFIG_FILENAME


config = Config()