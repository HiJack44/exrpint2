import os
import json


def load_config():
    path = os.path.join("templates", "config.json")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def save_config(data):
    path = os.path.join("templates", "config.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

config = load_config()
