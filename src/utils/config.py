import json


def get_config():
    with open("config.json", "r") as configfile:
        config = json.loads(configfile.read())
    return config
