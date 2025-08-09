import sys
import os

def run_test_module(module_name):
    """Run a test module and return True if all tests passed, False otherwise"""
    try:
        # Import the test module
        test_module = __import__(module_name, fromlist=['main'])
        
        # Run the main function of the test module
        print(f"Running tests for {module_name}...")
        test_module.main()
        print(f"All tests for {module_name} passed!\n")
        return True
    except Exception as e:
        print(f"Tests for {module_name} failed with error: {e}\n")
        return False

def main():
    print("Running all tests...\n")
    
    # Change to the tests directory
    tests_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(tests_dir)
    
    # Run all test modules
    test_modules = [
        "test_algo",
        "test_utils",
        "test_main"
    ]
    
    results = []
    for module in test_modules:
        result = run_test_module(module)
        results.append(result)
    
    # Print summary
    passed_count = sum(results)
    total_count = len(results)
    
    print(f"Test Results: {passed_count}/{total_count} test modules passed")
    
    if all(results):
        print("All tests passed!")
        return 0
    else:
        print("Some tests failed!")
        return 1

if __name__ == "__main__":
    sys.exit(main())