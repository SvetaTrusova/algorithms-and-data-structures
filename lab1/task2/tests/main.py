import unittest
from lab1.utils import insertion_sort


class TestInsertionSort1(unittest.TestCase):
    def test_empty_list(self):
        """Тест на пустой список"""
        data = []
        sorted_data, indexes = insertion_sort(len(data), data)
        self.assertEqual(sorted_data, [])
        self.assertEqual(indexes, [1])  # Индексы остаются на месте

    def test_single_element(self):
        """Тест на список с одним элементом"""
        data = [42]
        sorted_data, indexes = insertion_sort(len(data), data)
        self.assertEqual(sorted_data, [42])  # Список не изменится
        self.assertEqual(indexes, [1])  # Индекс остался на месте

    def test_sorted_list(self):
        """Тест на уже отсортированный список"""
        data = [1, 2, 3, 4, 5]
        sorted_data, indexes = insertion_sort(len(data), data)
        self.assertEqual(sorted_data, [1, 2, 3, 4, 5])  # Список уже отсортирован
        self.assertEqual(indexes, [1, 2, 3, 4, 5])  # Индексы должны быть на своих местах

    def test_reverse_order(self):
        """Тест на список в обратном порядке"""
        data = [5, 4, 3, 2, 1]
        sorted_data, indexes = insertion_sort(len(data), data)
        self.assertEqual(sorted_data, [1, 2, 3, 4, 5])  # Ожидаемый отсортированный список
        self.assertEqual(indexes, [1, 1, 1, 1, 1])  # Индексы будут следовать за сортировкой


if __name__ == "__main__":
    unittest.main()
