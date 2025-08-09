import sys
import os

# Add the parent directory to the path so we can import the modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.algo import findCheapestPrice

def test_findCheapestPrice_basic():
    """Test findCheapestPrice with basic input"""
    n = 4
    flights = [[0, 1, 100], [1, 2, 100], [2, 3, 100], [1, 3, 600], [2, 3, 200]]
    src = 0
    dst = 3
    k = 1
    
    result = findCheapestPrice(n, flights, src, dst, k)
    expected = 700  # Path: 0 -> 1 -> 2 -> 3 = 100 + 100 + 200 = 400, but with only 1 stop allowed, it's 0 -> 1 -> 3 = 700
    
    assert result == expected, f"Expected {expected}, but got {result}"
    print("test_findCheapestPrice_basic passed")

def test_findCheapestPrice_no_stops():
    """Test findCheapestPrice with no stops allowed"""
    n = 3
    flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    src = 0
    dst = 2
    k = 0
    
    result = findCheapestPrice(n, flights, src, dst, k)
    expected = 500  # Direct flight from 0 to 2
    
    assert result == expected, f"Expected {expected}, but got {result}"
    print("test_findCheapestPrice_no_stops passed")

def test_findCheapestPrice_with_stops():
    """Test findCheapestPrice with stops allowed"""
    n = 3
    flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    src = 0
    dst = 2
    k = 1
    
    result = findCheapestPrice(n, flights, src, dst, k)
    expected = 200  # Path: 0 -> 1 -> 2 = 100 + 100 = 200
    
    assert result == expected, f"Expected {expected}, but got {result}"
    print("test_findCheapestPrice_with_stops passed")

def test_findCheapestPrice_no_path():
    """Test findCheapestPrice when no path exists"""
    n = 3
    flights = [[0, 1, 100]]
    src = 0
    dst = 2
    k = 1
    
    result = findCheapestPrice(n, flights, src, dst, k)
    expected = -1  # No path from 0 to 2
    
    assert result == expected, f"Expected {expected}, but got {result}"
    print("test_findCheapestPrice_no_path passed")

def test_findCheapestPrice_complex():
    """Test findCheapestPrice with a more complex scenario"""
    n = 5
    flights = [[0, 1, 100], [1, 2, 100], [2, 3, 100], [3, 4, 100], [0, 4, 500]]
    src = 0
    dst = 4
    k = 3
    
    result = findCheapestPrice(n, flights, src, dst, k)
    expected = 400  # Path: 0 -> 1 -> 2 -> 3 -> 4 = 100 + 100 + 100 + 100 = 400
    
    assert result == expected, f"Expected {expected}, but got {result}"
    print("test_findCheapestPrice_complex passed")

def main():
    print("Running tests for algo.py...")
    test_findCheapestPrice_basic()
    test_findCheapestPrice_no_stops()
    test_findCheapestPrice_with_stops()
    test_findCheapestPrice_no_path()
    test_findCheapestPrice_complex()
    print("All tests for algo.py passed!")

if __name__ == "__main__":
    main()