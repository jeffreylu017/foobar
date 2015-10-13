import unittest
from foobar import badfilter

class TestBadFilter(unittest.TestCase):
    def test_badfilter1(self):
        odds = list(badfilter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6, 7]))
        self.assertEqual(odds, [2, 4, 6])

    def test_badfilter1(self):
        odds = list(badfilter(lambda x: x % 2 == 1, [1, 2, 3, 4, 5, 6, 7]))
        self.assertEqual(odds, [1, 3, 5, 7])

