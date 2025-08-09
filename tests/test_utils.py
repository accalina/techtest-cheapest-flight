import sys
import os
import json

# Add the parent directory to the path so we can import the modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.utils import read_json_file

def test_read_json_file_valid():
    """Test read_json_file with valid JSON file"""
    # Create a temporary valid JSON file for testing
    test_file = "temp_test.json"
    test_data = [
        {
            "n": 3,
            "flights": [[0, 1, 100], [1, 2, 100], [0, 2, 500]],
            "src": 0,
            "dst": 2,
            "k": 1
        }
    ]
    
    with open(test_file, "w") as f:
        json.dump(test_data, f)
    
    try:
        result = read_json_file(test_file)
        assert result == test_data, f"Expected {test_data}, but got {result}"
        print("test_read_json_file_valid passed")
    finally:
        # Clean up the temporary file
        if os.path.exists(test_file):
            os.remove(test_file)

def test_read_json_file_not_found():
    """Test read_json_file with non-existent file"""
    non_existent_file = "non_existent_file.json"
    
    try:
        result = read_json_file(non_existent_file)
        assert False, "Expected FileNotFoundError but none was raised"
    except FileNotFoundError as e:
        print("test_read_json_file_not_found passed")
    except Exception as e:
        assert False, f"Expected FileNotFoundError but got {type(e).__name__}: {e}"

def test_read_json_file_invalid():
    """Test read_json_file with invalid JSON file"""
    # Create a temporary invalid JSON file for testing
    test_file = "temp_invalid.json"
    
    with open(test_file, "w") as f:
        f.write("{ invalid json content }")
    
    try:
        result = read_json_file(test_file)
        assert False, "Expected ValueError but none was raised"
    except ValueError as e:
        print("test_read_json_file_invalid passed")
    except Exception as e:
        assert False, f"Expected ValueError but got {type(e).__name__}: {e}"
    finally:
        # Clean up the temporary file
        if os.path.exists(test_file):
            os.remove(test_file)

def main():
    print("Running tests for utils.py...")
    test_read_json_file_valid()
    test_read_json_file_not_found()
    test_read_json_file_invalid()
    print("All tests for utils.py passed!")

if __name__ == "__main__":
    main()