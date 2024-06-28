import json


def load_from_json_file(filename):
    with open(filename) as f:
        json.load(f)
