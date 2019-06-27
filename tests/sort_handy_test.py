import unittest

import __init__
import pyhandy.pyhandy as handy


class SortHandyTest(unittest.TestCase):
    def setUp(self):
        self.sort_handy = handy.SortHandy()
        self.is_sort = self.sort_handy.is_sorted

    def test_is_sort(self):
        self.assertFalse(self.is_sort([1, 7, 3, 2]))
        self.assertFalse(self.is_sort([0, 2, 3, 4, 1]))
        self.assertTrue(self.is_sort([1, 2, 3, 4, 5]))


if __name__ == "__main__":
    unittest.main()