import json


def load_operations(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)

    return data

