import sys
import os

# Add the parent directory to the path so we can import the modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from main import extract_flight_data

def test_extract_flight_data():
    """Test extract_flight_data function"""
    test_case = {
        "n": 3,
        "flights": [[0, 1, 100], [1, 2, 100], [0, 2, 500]],
        "src": 0,
        "dst": 2,
        "k": 1
    }
    
    n, flights, src, dst, k = extract_flight_data(test_case)
    
    assert n == 3, f"Expected n=3, but got {n}"
    assert flights == [[0, 1, 100], [1, 2, 100], [0, 2, 500]], f"Expected flights=[[0, 1, 100], [1, 2, 100], [0, 2, 500]], but got {flights}"
    assert src == 0, f"Expected src=0, but got {src}"
    assert dst == 2, f"Expected dst=2, but got {dst}"
    assert k == 1, f"Expected k=1, but got {k}"
    
    print("test_extract_flight_data passed")

def test_extract_flight_data_missing_key():
    """Test extract_flight_data function with missing key"""
    # Test case with missing 'k' key
    test_case = {
        "n": 3,
        "flights": [[0, 1, 100], [1, 2, 100], [0, 2, 500]],
        "src": 0,
        "dst": 2
        # 'k' key is missing
    }
    
    try:
        n, flights, src, dst, k = extract_flight_data(test_case)
        assert False, "Expected KeyError but none was raised"
    except KeyError as e:
        # Check if the error message is correct
        assert "Missing required key 'k'" in str(e), f"Expected error message about missing 'k' key, but got: {e}"
        print("test_extract_flight_data_missing_key passed")
    except Exception as e:
        assert False, f"Expected KeyError but got {type(e).__name__}: {e}"

def main():
    print("Running tests for main.py...")
    test_extract_flight_data()
    test_extract_flight_data_missing_key()
    print("All tests for main.py passed!")

if __name__ == "__main__":
    main()