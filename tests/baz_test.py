import unittest
from foobar import Baz

class BazTest(unittest.TestCase):
    def test_baz1(self):
        baz = Baz()
        self.assertEqual(baz.tested(0), 1)

