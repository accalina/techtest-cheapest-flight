
from src.algo import findCheapestPrice
from src.utils import read_json_file


def extract_flight_data(test_case):
    # Check if all required keys are present in the test case
    required_keys = ['n', 'flights', 'src', 'dst', 'k']
    for key in required_keys:
        if key not in test_case:
            raise KeyError(f"Missing required key '{key}' in test case data")
    
    n = test_case['n']
    flights = test_case['flights']
    src = test_case['src']
    dst = test_case['dst']
    k = test_case['k']
    return n, flights, src, dst, k

def main():
    flight_test_cases = read_json_file('question.json')
    for test_case in flight_test_cases:
        n, flights, src, dst, k = extract_flight_data(test_case)
        cheapest_price = findCheapestPrice(n, flights, src, dst, k)
        print(f"The cheapest price from {src} to {dst} with at most {k} stops is: {cheapest_price}")

if __name__ == '__main__':
    main()