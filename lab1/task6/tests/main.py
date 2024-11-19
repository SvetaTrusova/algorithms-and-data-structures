import unittest
from lab1.utils import bubblesort


class TestBubbleSort(unittest.TestCase):
    def test_empty_list(self):
        """Проверка на пустой список."""
        self.assertEqual(bubblesort(0, []), [])

    def test_single_element(self):
        """Проверка на список с одним элементом."""
        self.assertEqual(bubblesort(1, [42]), [42])

    def test_sorted_ascending(self):
        """Проверка на уже отсортированный список по возрастанию."""
        self.assertEqual(bubblesort(5, [1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_sorted_descending(self):
        """Проверка на список, отсортированный по убыванию."""
        self.assertEqual(bubblesort(5, [5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

        
if __name__ == "__main__":
    unittest.main()
