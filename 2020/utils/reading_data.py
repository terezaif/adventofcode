import re


def get_int_input_array(path: str) -> list:
    numbers = []
    with open(path, "r") as reader:
        # Read and print the entire file line by line
        for line in reader:
            numbers.append(int(line.strip()))
    return numbers


def get_string_input_array(path: str) -> list:
    strings = []
    with open(path, "r") as reader:
        # Read and print the entire file line by line
        for line in reader:
            strings.append(line.strip())
    return strings


def get_string_input_matrix(path: str) -> list:
    strings = []
    with open(path, "r") as reader:
        # Read and print the entire file line by line
        for line in reader:
            strings.append(list(line.strip()))
    return strings


def get_string_input_matrix_w_padding(path: str) -> list:
    strings = []
    with open(path, "r") as reader:
        # Read and print the entire file line by line
        for line in reader:
            line = list(line.strip())
            line.append("-")
            line.insert(0, "-")
            strings.append(line)

    length = len(strings[0])
    li = ["-"] * length
    strings.insert(0, li)
    strings.append(li)
    return strings


def get_string_input_matrix_r(path: str, regex: str) -> list:
    strings = []
    with open(path, "r") as reader:
        # Read and print the entire file line by line
        for line in reader:
            elems = list(re.findall(regex, line.strip())[0])
            strings.append(elems)
    return strings


def get_string_input_matrix_r_w_offset(path: str, regex: str, regex2: str) -> list:
    strings = []
    masks = []
    with open(path, "r") as reader:
        # Read and print the entire file line by line
        for line in reader:
            r1 = re.findall(regex, line.strip())
            r2 = re.findall(regex2, line.strip())
            if r1 != []:
                if len(masks) > 0:
                    strings.append(masks)
                masks = []
                masks.append(r1[0])
            else:
                masks.append(list(r2[0]))
    strings.append(masks)
    return strings
