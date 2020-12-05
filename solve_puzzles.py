from utils.reading_data import get_int_input_array, get_string_input_array
from days.day1 import get_product_of_2, get_product_of_3
from days.day2 import get_valid_password_count
from days.day2 import get_valid_password_policy2_count
from days.day3 import get_tree_count
from days.day4 import get_valid_passport_count
from days.day4 import get_valid_passport_validation_count
from days.day5 import get_top_seat, get_missing_seat

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
