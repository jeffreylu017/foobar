import unittest
import sys

SUITES = [
    'tests',
]

def test_suite(suite_dir):
    loader = unittest.TestLoader()
    suite = loader.discover('tests', pattern='*test.py')
    runner = unittest.TextTestRunner()
    result = runner.run(suite)
    return 0 if result.wasSuccessful() else 1

def main():
    failed = 0
    for suite in SUITES:
        failed += test_suite(suite)
    sys.exit(failed)

if __name__ == '__main__':
    main()
    loader = unittest.TestLoader()
    suite = loader.discover('tests', pattern='*test.py')
    runner = unittest.TextTestRunner()

