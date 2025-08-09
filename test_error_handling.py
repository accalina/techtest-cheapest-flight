import sys
import os
import json
from src.utils import read_json_file

def test_file_not_found():
    """Test read_json_file with a non-existent file"""
    print("Testing file not found error handling...")
    try:
        data = read_json_file("non_existent_file.json")
        print("ERROR: Should have raised FileNotFoundError")
        return False
    except FileNotFoundError as e:
        print(f"SUCCESS: Correctly caught FileNotFoundError: {e}")
        return True
    except Exception as e:
        print(f"ERROR: Caught unexpected exception: {e}")
        return False

def test_invalid_json():
    """Test read_json_file with invalid JSON content"""
    print("\nTesting invalid JSON error handling...")
    # Create a file with invalid JSON
    invalid_json_file = "invalid.json"
    with open(invalid_json_file, "w") as f:
        f.write("{ invalid json content }")
    
    try:
        data = read_json_file(invalid_json_file)
        print("ERROR: Should have raised ValueError for invalid JSON")
        # Clean up
        os.remove(invalid_json_file)
        return False
    except ValueError as e:
        print(f"SUCCESS: Correctly caught ValueError: {e}")
        # Clean up
        os.remove(invalid_json_file)
        return True
    except Exception as e:
        print(f"ERROR: Caught unexpected exception: {e}")
        # Clean up
        os.remove(invalid_json_file)
        return False

def test_valid_json():
    """Test read_json_file with valid JSON content"""
    print("\nTesting valid JSON handling...")
    try:
        data = read_json_file("question.json")
        print(f"SUCCESS: Successfully read valid JSON with {len(data)} test cases")
        return True
    except Exception as e:
        print(f"ERROR: Unexpected error with valid JSON: {e}")
        return False

def main():
    print("Testing error handling in read_json_file function\n")
    
    results = []
    results.append(test_file_not_found())
    results.append(test_invalid_json())
    results.append(test_valid_json())
    
    if all(results):
        print("\nAll tests passed!")
        return 0
    else:
        print("\nSome tests failed!")
        return 1

if __name__ == "__main__":
    sys.exit(main())