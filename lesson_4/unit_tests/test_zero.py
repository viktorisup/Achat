import unittest

from lesson_4.zero import zero

class TestZero(unittest.TestCase):

    def test_zero(self):
        self.assertIsInstance(zero('2', '3'), int)