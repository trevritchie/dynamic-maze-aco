import unittest
import sys
import os

# add the project root directory to Python path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

# create test suite
def create_test_suite():
    # discover all test files
    loader = unittest.TestLoader()
    start_dir = 'tests'
    suite = loader.discover(start_dir, pattern='test_*.py')
    return suite

if __name__ == '__main__':
    # run all tests
    suite = create_test_suite()
    runner = unittest.TextTestRunner()
    result = runner.run(suite)
    
    # exit with error code if tests failed
    sys.exit(not result.wasSuccessful())