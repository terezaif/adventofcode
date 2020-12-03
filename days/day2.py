
#how many passwords are not correct

#rule: first two numbers give the range, letter - count in range, password


def is_password_valid(entry:str) -> bool:    
    min, rest = entry.split('-', 1)
    max, rest = rest.split(' ',  1)
    letter, password = rest.split(': ', 1)
    count_letter = password.count(letter)
    if (count_letter >= int(min)) & (count_letter <= int(max)):
        return True
    #print("not valid")
    #print(f"Checking {entry}", min, max, letter, password, count_letter)
    return False

#Each policy actually describes two positions in the password, where 1 means the first character,
def is_password_valid_policy2(entry:str) -> bool:    
    min, rest = entry.split('-', 1)
    max, rest = rest.split(' ',  1)
    letter, password = rest.split(': ', 1)
    letters = list(password)

    count_letter = password.count(letter)
    if (letters[int(min)-1] == letter) ^ (letters[int(max)-1] == letter):
        return True
    #print("not valid")
    #print(f"Checking {entry}", min, max, letter, password, count_letter)
    return False


def get_valid_password_count(inputs:list)->int:
    correct_count =0
    for entry in inputs:
        correct_count += int(is_password_valid(entry))

    return  correct_count

def get_valid_password_policy2_count(inputs:list)->int:
    correct_count =0
    for entry in inputs:
        correct_count += int(is_password_valid_policy2(entry))

    return  correct_count




#input = get_string_input_array(path = 'data/day2.txt')
#print(get_invalid_password_count(input))