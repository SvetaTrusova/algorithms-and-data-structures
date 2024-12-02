from lab1.utils import memory_usage_process, read_input_7, write_output_7

path_input = "../txtf/input.txt"
path_output = "../txtf/output.txt"


def main():
    n, massive1 = read_input_7(path_input)
    massive = [(massive1[i], i + 1) for i in range(n)]
    massive = sorted(massive)

    write_output_7(path_output, massive, n)

print(f"Memory used by the current process: {memory_usage_process()} Megabytes")

if __name__ == '__main__':
    main()

