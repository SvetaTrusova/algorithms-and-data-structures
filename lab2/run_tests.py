import os
import sys
import unittest

# Добавляем корневую директорию проекта в sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def run_all_tests():
    suite = unittest.TestSuite()

    # Путь к корневой директории проекта
    base_dir = os.path.abspath(os.path.dirname(__file__))
    sys.path.append(base_dir)  # Добавляем проект в sys.path для корректного импорта

    # Прямо указываем каждый тестовый файл
    test_files = [
        'lab2.task1.tests.test_2_1',
        'lab2.task2.tests.test_2_2',
        'lab2.task3.tests.test_2_3',
        'lab2.task4.tests.test_2_4',
        'lab2.task5.tests.test_2_5',
        'lab2.task10.tests.test_2_10',
    ]

    # Добавляем тесты вручную
    for test_file in test_files:
        try:
            suite.addTest(unittest.defaultTestLoader.loadTestsFromName(test_file))
        except ModuleNotFoundError as e:
            print(f"Ошибка при добавлении теста {test_file}: {e}")

    # Запуск тестов
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == "__main__":
    run_all_tests()
