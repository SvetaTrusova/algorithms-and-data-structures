from lab1.utils import read_input_7, write_output_7
import unittest
from unittest.mock import mock_open, patch


class TestFunctions(unittest.TestCase):

    # Тест для read_input_7
    @patch('builtins.open', mock_open(read_data="5\n1.1 2.2 3.3 4.4 5.5"))
    def test_read_input_7(self):
        path_input = 'fake_path_input.txt'
        expected_n = 5
        expected_massive1 = [1.1, 2.2, 3.3, 4.4, 5.5]

        n, massive1 = read_input_7(path_input)

        # Проверка правильности возвращаемых данных
        self.assertEqual(n, expected_n)
        self.assertEqual(massive1, expected_massive1)

    # Тест для write_output_7
    class TestFunctions(unittest.TestCase):
        @patch('builtins.open', mock_open())
        def test_write_output_7(self, mock_file):
            path_output = 'fake_path_output.txt'
            massive = [(0, 1.1), (1, 2.2), (2, 3.3), (3, 4.4), (4, 5.5)]  # Пример массива
            n = 5  # Число элементов в массиве

            # Мокируем запись в файл
            write_output_7(path_output, massive, n)

            # Проверяем, что файл был открыт с правильными параметрами
            mock_file.assert_called_once_with(path_output, 'w')

            # Получаем строку, которую пытался записать файл
            handle = mock_file()

            # Проверяем, что в файл записаны правильные данные
            handle.write.assert_any_call("1.1 ")
            handle.write.assert_any_call("3.3 ")
            handle.write.assert_any_call("5.5")

            # Получаем все вызовы write и проверяем, что данные записаны в нужном формате
            written_data = ''.join(call[0][0] for call in handle.write.call_args_list)
            self.assertEqual(written_data.strip(), "1.1 3.3 5.5")


if __name__ == '__main__':
    unittest.main()
