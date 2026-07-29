from pathlib import Path
import json


class BridgeManager:

    def __init__(self):

        self.folder = (
            Path.home() /
            "Documents" /
            "SU2Bridge"
        )

        self.file = self.folder / "bridge.json"

    def create(self):

        self.folder.mkdir(
            parents=True,
            exist_ok=True
        )

        if not self.file.exists():

            self.save(
                {
                    "version": 1,
                    "status": "idle",
                    "project": "",
                    "model": "",
                    "materials": ""
                }
            )

    def load(self):

        if not self.file.exists():
            return None

        with open(
            self.file,
            "r",
            encoding="utf8"
        ) as f:

            return json.load(f)

    def save(self, data):

        with open(
            self.file,
            "w",
            encoding="utf8"
        ) as f:

            json.dump(
                data,
                f,
                indent=4
            )


bridge = BridgeManager()