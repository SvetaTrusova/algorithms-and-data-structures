from lab1.utils import insertion_sort, read_input, write_output, memory_usage_process

def main():
    n, data = read_input()
    sorted_data, sorted_indexes = insertion_sort(n, data)
    str_norm_sorted_data = ' '.join(map(str, sorted_data))  # Преобразуем элементы списка в строку, разделяя пробелами
    str_norm_sorted_indexes = ' '.join(map(str, sorted_indexes))  # То же для второго массива
    output_string = str_norm_sorted_indexes + '\n' + str_norm_sorted_data + '\n'
    if 1 <= n <= 10 ** 3:
        write_output(output_string)
    else:
        print('Введенные данные не соответствуют условию')


print(f"Memory used by the current process: {memory_usage_process()} Megabytes")


if __name__ == '__main__':
    main()


