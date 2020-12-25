def is_password_valid(entry: str) -> bool:
    min, rest = entry.split("-", 1)
    max, rest = rest.split(" ", 1)
    letter, password = rest.split(": ", 1)
    count_letter = password.count(letter)
    if (count_letter >= int(min)) & (count_letter <= int(max)):
        return True
    return False


def is_password_valid_policy2(entry: str) -> bool:
    min, rest = entry.split("-", 1)
    max, rest = rest.split(" ", 1)
    letter, password = rest.split(": ", 1)
    letters = list(password)
    if (letters[int(min) - 1] == letter) ^ (letters[int(max) - 1] == letter):
        return True
    return False


def get_valid_password_count(inputs: list) -> int:
    correct_count = 0
    for entry in inputs:
        correct_count += int(is_password_valid(entry))

    return correct_count


def get_valid_password_policy2_count(inputs: list) -> int:
    correct_count = 0
    for entry in inputs:
        correct_count += int(is_password_valid_policy2(entry))

    return correct_count
