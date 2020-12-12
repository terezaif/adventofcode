from utils.reading_data import (
    get_int_input_array,
    get_string_input_array,
    get_string_input_matrix_w_padding,
    get_string_input_matrix_r,
)
from days.day1 import get_product_of_2, get_product_of_3
from days.day2 import get_valid_password_count
from days.day2 import get_valid_password_policy2_count
from days.day3 import get_tree_count
from days.day4 import get_valid_passport_count
from days.day4 import get_valid_passport_validation_count
from days.day5 import get_top_seat, get_missing_seat
from days.day6 import get_questions_count
from days.day6 import get_questions_everyone_count
from days.day7 import get_bags
from days.day7 import get_bags_2
from days.day8 import get_acc, get_acc_2
from days.day9 import get_first_number, get_list_ends
from days.day10 import get_diff
from days.day10 import get_diff_2
from days.day11 import get_seat_count
from days.day11 import get_seat_count_2
from days.day12 import get_distance
from days.day12 import get_distance_2

print("Puzzle for day12:")
regex = r"(\w)(\d*)"
input12 = get_string_input_matrix_r(path="data/day12.txt", regex=regex)

print(get_distance(input12))
print(get_distance_2(input12))


# print("Puzzle for day11:")
# input11 = get_string_input_matrix_w_padding(path="data/day11.txt")
# print(get_seat_count(input11))
# input11 = get_string_input_matrix_w_padding(path="data/day11.txt")
# print(get_seat_count_2(input11))

print("Puzzle for day10:")
input10 = get_int_input_array(path="data/day10.txt")
print(get_diff(input10))
print(get_diff_2(input10))

print("Puzzle for day9:")
input9 = get_int_input_array(path="data/day9.txt")
print(get_first_number(25, input9))
print(get_list_ends(556543474, input9))

print("Puzzle for day8:")
input8 = get_string_input_array(path="data/day8.txt")
print(get_acc(input8))
print(get_acc_2(input8))

print("Puzzle for day7:")
input7 = get_string_input_array(path="data/day7.txt")
print(get_bags(input7))
print(get_bags_2(input7))

print("Puzzle for day6:")
input6 = get_string_input_array(path="data/day6.txt")
print(get_questions_count(input6))
print(get_questions_everyone_count(input6))

print("Puzzle for day5:")
input5 = get_string_input_array(path="data/day5.txt")
print(get_top_seat(input5))
print(get_missing_seat(input5))

print("Puzzle for day4:")
input4 = get_string_input_array(path="data/day4.txt")
print(get_valid_passport_count(input4))
print(get_valid_passport_validation_count(input4))

print("Puzzle for day3:")
input3 = get_string_input_array(path="data/day3.txt")
print(get_tree_count(3, 1, input3))
all_trees = (
    get_tree_count(1, 1, input3)
    * get_tree_count(3, 1, input3)
    * get_tree_count(5, 1, input3)
    * get_tree_count(7, 1, input3)
    * get_tree_count(1, 2, input3)
)
print(all_trees)


print("Puzzle for day2: ")
input2 = get_string_input_array(path="data/day2.txt")
print(get_valid_password_count(input2))
print(get_valid_password_policy2_count(input2))


print("Puzzle for day1: ")
numbers1 = get_int_input_array(path="data/day1.txt")
print(get_product_of_2(numbers1))
print(get_product_of_3(numbers1))
