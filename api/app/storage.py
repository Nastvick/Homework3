import json


def get_data():
    with open('storage.json', 'r') as f:
        return  json.load(f)

def store_data(data):
    with open('storage.json', 'w') as f:
        json.dump(data, f)