def get_int_input_array(path: str)->list:
    numbers = []
    with open(path, 'r') as reader:
    # Read and print the entire file line by line
     for line in reader:
        numbers.append(int(line.strip()))
    return numbers

def get_string_input_array(path: str)->list:
    strings = []
    with open(path, 'r') as reader:
    # Read and print the entire file line by line
     for line in reader:
        strings.append(line.strip())
    return strings