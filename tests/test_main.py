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

def test_extract_flight_data_invalid_n():
    """Test extract_flight_data function with invalid n value"""
    test_case = {
        "n": "invalid",
        "flights": [[0, 1, 100], [1, 2, 100], [0, 2, 500]],
        "src": 0,
        "dst": 2,
        "k": 1
    }
    
    try:
        n, flights, src, dst, k = extract_flight_data(test_case)
        assert False, "Expected ValueError but none was raised"
    except ValueError as e:
        # Check if the error message is correct
        assert "Invalid value for 'n'" in str(e), f"Expected error message about invalid 'n' value, but got: {e}"
        print("test_extract_flight_data_invalid_n passed")
    except Exception as e:
        assert False, f"Expected ValueError but got {type(e).__name__}: {e}"

def test_extract_flight_data_invalid_flights():
    """Test extract_flight_data function with invalid flights value"""
    test_case = {
        "n": 3,
        "flights": "invalid",
        "src": 0,
        "dst": 2,
        "k": 1
    }
    
    try:
        n, flights, src, dst, k = extract_flight_data(test_case)
        assert False, "Expected ValueError but none was raised"
    except ValueError as e:
        # Check if the error message is correct
        assert "Invalid value for 'flights'" in str(e), f"Expected error message about invalid 'flights' value, but got: {e}"
        print("test_extract_flight_data_invalid_flights passed")
    except Exception as e:
        assert False, f"Expected ValueError but got {type(e).__name__}: {e}"

def test_extract_flight_data_invalid_src():
    """Test extract_flight_data function with invalid src value"""
    test_case = {
        "n": 3,
        "flights": [[0, 1, 100], [1, 2, 100], [0, 2, 500]],
        "src": "invalid",
        "dst": 2,
        "k": 1
    }
    
    try:
        n, flights, src, dst, k = extract_flight_data(test_case)
        assert False, "Expected ValueError but none was raised"
    except ValueError as e:
        # Check if the error message is correct
        assert "Invalid value for 'src'" in str(e), f"Expected error message about invalid 'src' value, but got: {e}"
        print("test_extract_flight_data_invalid_src passed")
    except Exception as e:
        assert False, f"Expected ValueError but got {type(e).__name__}: {e}"

def test_extract_flight_data_invalid_dst():
    """Test extract_flight_data function with invalid dst value"""
    test_case = {
        "n": 3,
        "flights": [[0, 1, 100], [1, 2, 100], [0, 2, 500]],
        "src": 0,
        "dst": "invalid",
        "k": 1
    }
    
    try:
        n, flights, src, dst, k = extract_flight_data(test_case)
        assert False, "Expected ValueError but none was raised"
    except ValueError as e:
        # Check if the error message is correct
        assert "Invalid value for 'dst'" in str(e), f"Expected error message about invalid 'dst' value, but got: {e}"
        print("test_extract_flight_data_invalid_dst passed")
    except Exception as e:
        assert False, f"Expected ValueError but got {type(e).__name__}: {e}"

def test_extract_flight_data_invalid_k():
    """Test extract_flight_data function with invalid k value"""
    test_case = {
        "n": 3,
        "flights": [[0, 1, 100], [1, 2, 100], [0, 2, 500]],
        "src": 0,
        "dst": 2,
        "k": "invalid"
    }
    
    try:
        n, flights, src, dst, k = extract_flight_data(test_case)
        assert False, "Expected ValueError but none was raised"
    except ValueError as e:
        # Check if the error message is correct
        assert "Invalid value for 'k'" in str(e), f"Expected error message about invalid 'k' value, but got: {e}"
        print("test_extract_flight_data_invalid_k passed")
    except Exception as e:
        assert False, f"Expected ValueError but got {type(e).__name__}: {e}"

def main():
    print("Running tests for main.py...")
    test_extract_flight_data()
    test_extract_flight_data_missing_key()
    test_extract_flight_data_invalid_n()
    test_extract_flight_data_invalid_flights()
    test_extract_flight_data_invalid_src()
    test_extract_flight_data_invalid_dst()
    test_extract_flight_data_invalid_k()
    print("All tests for main.py passed!")

if __name__ == "__main__":
    main()