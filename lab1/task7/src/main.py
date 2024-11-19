from lab1.utils import memory_usage_process

path_input = "../txtf/input.txt"
path_output = "../txtf/output.txt"
def main():
    with open(path_input, 'r') as f:
        n = int(f.readline())
        massive1 = [float(a) for a in f.readline().split()]
        massive = []
        cnt = 0
        for i in massive1:
            cnt += 1
            massive.append([i, cnt])
    massive = sorted(massive)

    with open(path_output, 'w') as f:
        f.write(str(massive[0][1]))
        f.write(' ')
        f.write(str(massive[n // 2][1]))
        f.write(' ')
        f.write(str(massive[-1][1]))

print(f"Memory used by the current process: {memory_usage_process()} Megabytes")

if __name__ == '__main__':
    main()
