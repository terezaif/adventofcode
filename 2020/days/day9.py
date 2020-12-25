def get_first_number(pre: int, input: list) -> int:
    for i in range(pre, len(input) - pre):
        if check_if_pairs(input[i : pre + i], input[pre + i]) is False:
            return input[pre + i]
    return 0


def check_if_pairs(numbers: list, x: int):
    for index1 in range(0, len(numbers)):
        number1 = numbers[index1]
        for index2 in range(index1, len(numbers)):
            number2 = numbers[index2]
            if number1 + number2 == x:
                return True
    return False


def get_list_ends(x, input: list) -> int:
    for i in range(2, len(input) - 2):
        l, r = find_range(i, input, x)
        if l + r != 0:
            return l + r
    return 10


def find_range(le, numbers, x):
    for i in range(0, len(numbers) - le):
        if sum(numbers[i : le + i]) == x:
            return min(numbers[i : le + i]), max(numbers[i : le + i])

    return 0, 0
