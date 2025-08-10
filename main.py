
from src.algo import findCheapestPrice
from src.utils import read_json_file


def extract_flight_data(test_case):
    # Check if all required keys are present in the test case
    required_keys = ['n', 'flights', 'src', 'dst', 'k']
    for key in required_keys:
        if key not in test_case:
            raise KeyError(f"Missing required key '{key}' in test case data")
    
    # Validate the format of the values
    # n should be an integer
    if not isinstance(test_case['n'], int):
        raise ValueError(f"Invalid value for 'n': expected integer, got {type(test_case['n'])}")
    
    # flights should be a list of lists, where each inner list has 3 elements (from, to, price) and all elements are integers
    if not isinstance(test_case['flights'], list):
        raise ValueError(f"Invalid value for 'flights': expected list, got {type(test_case['flights'])}")
    
    for i, flight in enumerate(test_case['flights']):
        if not isinstance(flight, list):
            raise ValueError(f"Invalid value for 'flights[{i}]': expected list, got {type(flight)}")
        if len(flight) != 3:
            raise ValueError(f"Invalid value for 'flights[{i}]': expected list with 3 elements, got {len(flight)}")
        for j, value in enumerate(flight):
            if not isinstance(value, int):
                raise ValueError(f"Invalid value for 'flights[{i}][{j}]': expected integer, got {type(value)}")
    
    # src should be an integer
    if not isinstance(test_case['src'], int):
        raise ValueError(f"Invalid value for 'src': expected integer, got {type(test_case['src'])}")
    
    # dst should be an integer
    if not isinstance(test_case['dst'], int):
        raise ValueError(f"Invalid value for 'dst': expected integer, got {type(test_case['dst'])}")
    
    # k should be an integer
    if not isinstance(test_case['k'], int):
        raise ValueError(f"Invalid value for 'k': expected integer, got {type(test_case['k'])}")
    
    n = test_case['n']
    flights = test_case['flights']
    src = test_case['src']
    dst = test_case['dst']
    k = test_case['k']
    return n, flights, src, dst, k

def main():
    try:
        flight_test_cases = read_json_file('question.json')
    except Exception as e:
        print(f"Error reading flight data: {e}")
        return
    
    for i, test_case in enumerate(flight_test_cases):
        try:
            n, flights, src, dst, k = extract_flight_data(test_case)
            cheapest_price = findCheapestPrice(n, flights, src, dst, k)
            print(f"The cheapest price from {src} to {dst} with at most {k} stops is: {cheapest_price}")
        except Exception as e:
            print(f"Error processing test case {i}: {e}")
            continue

if __name__ == '__main__':
    main()