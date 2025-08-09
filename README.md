# Tech Test - Cheapest Flight Finder

## Program Description and Objective

This program finds the cheapest flight price between two cities with a limited number of stops. It implements a modified breadth-first search (BFS) algorithm to explore all possible paths while respecting the maximum number of stops constraint.

The objective is to provide an efficient solution for finding the optimal cost route between cities, which is a common problem in travel planning and logistics.

## Program Requirements

- Python 3.6 or higher
- No external dependencies (uses only Python standard library)

## How to Run the Program

1. Ensure you have Python 3.6+ installed on your system
2. Navigate to the project directory in your terminal
3. Run the main script:

```bash
python main.py
```

The program will read flight data from `question.json` and output the cheapest price for each test case.

## How to Test the Program

### Running All Tests

To run all tests, execute the test runner script:

```bash
python tests/run_tests.py
```

### Running Individual Test Files

You can also run individual test files directly:

```bash
python tests/test_algo.py
python tests/test_utils.py
python tests/test_main.py
```

### Test Coverage

The tests cover:
- Normal scenarios for finding the cheapest flight prices
- Edge cases like no available paths or no stops allowed
- Error handling for file not found and invalid JSON scenarios
- All utility functions for data processing

## Project Structure

```
techtest-cheapest-flight/
├── main.py                 # Main entry point for the application
├── question.json           # Test data with flight information
├── README.md               # Project documentation
├── .gitignore              # Git ignore file
├── src/                    # Source code directory
│   ├── algo.py             # Algorithm implementation for finding cheapest flights
│   └── utils.py            # Utility functions for file handling
└── tests/                  # Test directory
    ├── run_tests.py        # Test runner script
    ├── test_algo.py        # Tests for algorithm functions
    ├── test_main.py        # Tests for main functions
    └── test_utils.py       # Tests for utility functions
```

## Algorithm Explanation

The program uses a modified breadth-first search (BFS) algorithm to find the cheapest flight path:

1. It builds a graph representation of all flights
2. It uses a queue to explore paths with increasing numbers of stops
3. It tracks the minimum cost to reach each city
4. It stops exploring when the maximum number of stops is reached

The time complexity is O(E * K) where E is the number of flights and K is the maximum number of stops.
The space complexity is O(N) where N is the number of cities.
