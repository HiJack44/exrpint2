import os
import json


def load_config():
    path = os.path.join("templates", "config.json")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


config = load_config()
