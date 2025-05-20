import json

def load_data(filepath):
    with open(filepath, "r") as f:
        return json.load(f)

def save_data(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f, indent=4)