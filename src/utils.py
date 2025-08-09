import json

def read_json_file(file_path):
    """ Reads a JSON file and returns the data. """
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data