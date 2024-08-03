# loc class that contains the paths to the different directories.

import json
import os


def get_home_dir():
    return os.path.expanduser("~")


class Loc:
    def __init__(self):
        self.APP_NAME = "loc-maker"
        self.HOME_DIR = get_home_dir()
        self.FILE_NAME = os.path.join(self.HOME_DIR, ".loc.json")
        self.dirs = ["bin", "dependencies", "config", "scripts", "workspace"]
        self.paths = {}

    def write(self):
        if any([self.paths.get(i, None) is None for i in self.dirs]):
            print(self.paths)
            return False
        with open(self.FILE_NAME, "w") as f:
            json.dump(self.paths, f, indent=4)

    def read(self):
        if os.path.exists(self.FILE_NAME):
            with open(self.FILE_NAME, "r") as f:
                self.paths = json.load(f)
        else:
            print("No .loc.json file found in home directory.")

    def empty(self):
        return self.paths == {}

    def get(self, name):
        return self.paths.get(name, None)

    def set(self, name, value):
        self.paths[name] = value

    def get_required(self):
        return self.dirs

    def valid(self, name):
        return name not in list(self.paths.keys())

    def create_dirs(self):
        for path in self.paths:
            if os.path.exists(self.paths[path]) is False:
                os.mkdir(self.paths[path])

    def __str__(self):
        return str(self.paths)

    def __repr__(self):
        return str(self.paths)
