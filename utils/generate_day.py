import sys
import os


def create_day_file(day: int):
    filename = f"days/day{day}.py"
    code = [
        "def get_count(input:list)-> int:\n",
        "\treturn 10",
        "\n",
        "\n",
        "def get_count_2(input:list)-> int:\n",
        "\treturn 10\n",
    ]
    file = open(filename, "w")
    file.writelines(code)
    file.close()


def create_day_test_file(day: int):
    filename = f"test/test_day{day}.py"
    code = [
        f"from days.day{day} import get_count\n",
        f"from days.day{day} import get_count_2\n",
        "from utils.reading_data import get_int_input_array\n",
        "\n",
        f'input = get_string_input_array(path="test/data/day{day}.txt")\n',
        "\n",
        "def test_get_count():\n",
        "\texpected = 10\n",
        "\tactual = get_count(input)\n",
        "\tassert expected == actual\n",
        "\n",
        "def test_get_count_2():\n",
        "\texpected = 10\n",
        "\tactual = get_count_2(input)\n",
        "\tassert expected == actual\n",
    ]
    file = open(filename, "w")
    file.writelines(code)
    file.close()


def get_puzzle_call_code(day: int):
    code = (
        f"from days.day{day} import get_count\n"
        f"from days.day{day} import get_count_2\n"
        "\n"
        f'print("Puzzle for day{day}:")\n'
        f'input{day} = get_string_input_array(path="data/day{day}.txt")\n'
        f"print(get_count(input{day}))\n"
        f"print(get_count_2(input{day}))\n"
    )

    return code


def main(argv):

    day = int(argv[0])
    data_file = f"data/day{day}.txt"
    if os.path.exists(data_file):
        print("day exists")
        return
    print("generating files for day ", day)
    cmd = f"touch data/day{day}.txt"
    os.system(cmd)
    cmd = f"touch test/data/day{day}.txt"
    os.system(cmd)
    create_day_file(day)
    create_day_test_file(day)
    print("\n\nCode for puzzle script: \n\n")
    print(get_puzzle_call_code(day))


if __name__ == "__main__":
    main(sys.argv[1:])
