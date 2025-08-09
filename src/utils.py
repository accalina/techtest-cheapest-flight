import json
import os

def read_json_file(file_path):
    """ Reads a JSON file and returns the data. """
    # Check if file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    try:
        with open(file_path, 'r') as file:
            json_data = json.load(file)
        return json_data
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON in file {file_path}: {str(e)}")
    except Exception as e:
        raise Exception(f"Error reading file {file_path}: {str(e)}")