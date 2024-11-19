import unittest
from lab1.utils import selectionsort


class TestSelectionSort(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(selectionsort([]), [])

    def test_single_element(self):
        self.assertEqual(selectionsort([42]), [42])

    def test_all_elements_equal(self):
        self.assertEqual(selectionsort([5, 5, 5, 5]), [5, 5, 5, 5])

    def test_already_sorted_ascending(self):
        self.assertEqual(selectionsort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_sorted_descending(self):
        self.assertEqual(selectionsort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])


if __name__ == "__main__":
    unittest.main()
