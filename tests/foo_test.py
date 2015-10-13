import unittest
from foobar import foo

class TestFoo(unittest.TestCase):

    def test_foo1(self):
        self.assertEqual(foo(1, 2), 3)
        self.assertEqual(foo(1, 3), 4)

