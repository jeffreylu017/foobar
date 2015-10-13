import unittest
from foobar import filter

class TestFilter(unittest.TestCase):
    def test_filter1(self):
        odds = list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6, 7]))
        self.assertEqual(odds, [2, 4, 6])

    def test_filter1(self):
        odds = list(filter(lambda x: x % 2 == 1, [1, 2, 3, 4, 5, 6, 7]))
        self.assertEqual(odds, [1, 3, 5, 7])

