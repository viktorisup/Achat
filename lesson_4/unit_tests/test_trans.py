import unittest
from lesson_4.trans import num_translate


class TestTrans(unittest.TestCase):
    def test_trans(self):
        self.assertEqual(num_translate('one'), 'один')
