# Cheapest Flight Finder - Documentation

## Overview

The Cheapest Flight Finder is a Python application that finds the cheapest flight price between two cities with a limited number of stops. It implements a modified breadth-first search (BFS) algorithm to explore all possible paths while respecting the maximum number of stops constraint.

The objective is to provide an efficient solution for finding the optimal cost route between cities, which is a common problem in travel planning and logistics.

## Features

- Finds the cheapest flight price between two cities with a limited number of stops
- Implements a modified BFS algorithm for efficient path exploration
- Robust error handling for file operations and data validation
- Comprehensive test suite covering normal scenarios, edge cases, and error conditions
- No external dependencies (uses only Python standard library)

## Requirements

- Python 3.9 or higher
- No external dependencies required

## Installation

1. Ensure you have Python 3.9+ installed on your system
2. Clone or download the repository
3. No additional installation steps are required as the program uses only Python standard library modules

## How to Run the Program

1. Navigate to the project directory in your terminal
2. Run the main script:

```bash
python main.py
```

The program will read flight data from `question.json` and output the cheapest price for each test case.

## How to Run Tests

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

## Algorithm Explanation

The program uses a modified breadth-first search (BFS) algorithm to find the cheapest flight path:

1. It builds a graph representation of all flights
2. It uses a queue to explore paths with increasing numbers of stops
3. It tracks the minimum cost to reach each city
4. It stops exploring when the maximum number of stops is reached

The time complexity is O(E * K) where E is the number of flights and K is the maximum number of stops.
The space complexity is O(N) where N is the number of cities.

## Project Structure

```
techtest-cheapest-flight/
├── main.py                 # Main entry point for the application
├── question.json           # Test data with flight information
├── documentation.md        # Project documentation
├── README.md               # Project overview and basic instructions
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

## Main Components

### main.py

The main entry point of the application that:
- Reads flight data from `question.json`
- Processes each test case
- Calls the algorithm to find the cheapest price
- Handles errors gracefully

Key functions:
- `extract_flight_data()`: Validates and extracts flight data from test cases
- `main()`: Main execution function that processes all test cases

### src/algo.py

Contains the core algorithm implementation:
- `findCheapestPrice()`: Implements the modified BFS algorithm to find the cheapest flight price

The function takes the following parameters:
- `n`: Number of cities
- `flights`: List of flights [from, to, price]
- `src`: Source city
- `dst`: Destination city
- `k`: Maximum number of stops allowed

Returns the cheapest price to reach the destination, or -1 if not possible.

### src/utils.py

Contains utility functions:
- `read_json_file()`: Reads a JSON file and returns the data with proper error handling

### question.json

Contains test data with flight information in the following format:
```json
[
    {
        "n": 4,
        "flights": [[0, 1, 100], [1, 2, 100], [2, 3, 100], [1, 3, 600]],
        "src": 0,
        "dst": 3,
        "k": 1
    }
]
```

Where:
- `n`: Number of cities (numbered from 0 to n-1)
- `flights`: List of flights, each represented as [from, to, price]
- `src`: Source city
- `dst`: Destination city
- `k`: Maximum number of stops allowed

## Error Handling and Validation

The program includes robust error handling to ensure that:
- Required keys are present in the JSON data
- Files exist before attempting to read them
- JSON data is valid before processing
- Values in the JSON data are of the correct type and format
- The program gracefully handles errors and continues processing other test cases

## Usage Examples

### Example 1: Basic Usage

Given the following flight data:
```json
{
    "n": 3,
    "flights": [[0, 1, 100], [1, 2, 100], [0, 2, 500]],
    "src": 0,
    "dst": 2,
    "k": 1
}
```

The program will find the cheapest price from city 0 to city 2 with at most 1 stop:
- Direct flight: 0 -> 2 costs 500
- With one stop: 0 -> 1 -> 2 costs 200
- Result: 200 (cheaper path with one stop)

### Example 2: No Stops Allowed

Given the following flight data:
```json
{
    "n": 3,
    "flights": [[0, 1, 100], [1, 2, 100], [0, 2, 500]],
    "src": 0,
    "dst": 2,
    "k": 0
}
```

The program will find the cheapest price from city 0 to city 2 with no stops allowed:
- Only direct flight is allowed: 0 -> 2 costs 500
- Result: 500 (direct flight)

## Contributing

This project is designed as a technical test and is not currently accepting contributions. However, you are welcome to fork the repository and modify it for your own use.

## License

This project is provided as a technical test and does not have a specific license. Please check with the repository owner for licensing information if you plan to use this code in a commercial project.