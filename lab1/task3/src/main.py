from lab1.utils import insertionsort_not_increasing, read_input, write_output, normVid, memory_usage_process


def main():
    n, data = read_input()
    sorted_data = insertionsort_not_increasing(data)
    norm_sorted_data = normVid(sorted_data)
    write_output(norm_sorted_data)


print(f"Memory used by the current process: {memory_usage_process()} Megabytes")


if __name__ == '__main__':
    main()
