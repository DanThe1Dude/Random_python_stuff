import json


def load(file_to_load_from):
    with open(file_to_load_from, "r") as f:
        content = f.read()
        return json.loads(content)


print(load("test_file.json"))