import unittest
from lab1.utils import insertionsort_not_increasing


class TestInsertionSortNotIncrease(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(insertionsort_not_increasing([]), [])

    def test_single_element(self):
        self.assertEqual(insertionsort_not_increasing([42]), [42])

    def test_all_elements_equal(self):
        self.assertEqual(insertionsort_not_increasing([5, 5, 5, 5]), [5, 5, 5, 5])

    def test_already_sorted_descending(self):
        self.assertEqual(insertionsort_not_increasing([9, 7, 5, 3, 1]), [9, 7, 5, 3, 1])

    def test_sorted_ascending(self):
        self.assertEqual(insertionsort_not_increasing([1, 3, 5, 7, 9]), [9, 7, 5, 3, 1])


if __name__ == "__main__":
    unittest.main()
