path_input = "../txtf/input.txt"
path_output = "../txtf/output.txt"

def write_file(string: str) -> None:
    with open(path_output, "w", encoding="utf-8") as file:
        file.write(string)


def read_file() -> str:
    with open(path_input, "r") as file:
        return file.read()