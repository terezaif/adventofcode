from utils.reading_data import get_int_input_array, get_string_input_array
from days.day1 import get_product_of_2, get_product_of_3
from days.day2 import get_valid_password_count
from days.day2 import get_valid_password_policy2_count
from days.day3 import get_tree_count

print("Puzzle for day1: ")
numbers1 = get_int_input_array(path="data/day1.txt")
print(get_product_of_2(numbers1))
print(get_product_of_3(numbers1))

print("Puzzle for day2: ")
input2 = get_string_input_array(path="data/day2.txt")
print(get_valid_password_count(input2))
print(get_valid_password_policy2_count(input2))

print("Puzzle for day3:")
input3 = get_string_input_array(path="data/day3.txt")
print(get_tree_count(3, 1, input3))
all_trees = (
    get_tree_count(1, 1, input3)
    * get_tree_count(3, 1, input3)
    * get_tree_count(5, 1, input3)
)
all_trees *= get_tree_count(7, 1, input3) * get_tree_count(1, 2, input3)
print(all_trees)
