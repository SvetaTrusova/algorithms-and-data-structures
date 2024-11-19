import unittest
from lab1.utils import insertionsort


class TestInsertionSort(unittest.TestCase):
    def test_insertion_sort(self):
        """Проверка сортировки вставками"""
        sorted_arr = insertionsort([1, 8, 4, 2, 3, 7, 5, 6, 9, 0])
        self.assertEqual(sorted_arr, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_empty_list(self):
        """Тест на пустой список"""
        self.assertEqual(insertionsort([]), [])

    def test_single_element(self):
        """Тест на список из одного элемента"""
        self.assertEqual(insertionsort([42]), [42])

    def test_sorted_list(self):
        """Тест на уже отсортированный список"""
        self.assertEqual(insertionsort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reverse_order(self):
        """Тест на список в обратном порядке"""
        self.assertEqual(insertionsort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_all_equal_elements(self):
        """Тест на список с одинаковыми элементами"""
        self.assertEqual(insertionsort([7, 7, 7, 7, 7]), [7, 7, 7, 7, 7])


if __name__ == "__main__":
    unittest.main()
