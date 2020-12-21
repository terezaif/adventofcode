from utils.reading_data import (
    get_int_input_array,
    get_string_input_array,
    get_string_input_matrix_w_padding,
    get_string_input_matrix_r,
    get_string_input_matrix_r_w_offset,
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
from days.day13 import get_bus
from days.day13 import get_bus_2
from days.day14 import get_memsum
from days.day14 import get_memsum_2
from days.day15 import get_nth_spoken
from days.day16 import get_sum_wrong
from days.day16 import get_prod_right
from days.day17 import get_active_cubes
from days.day18 import get_sum_arithmetics
from days.day19 import get_msg_count
from days.day19 import get_msg_count_2
from days.day20 import get_corners
from days.day21 import get_goodfood_count
from days.day21 import get_badfood

print("Puzzle for day21:")
input21 = get_string_input_array(path="data/day21.txt")
print(get_goodfood_count(input21))
print(get_badfood(input21))

# print("Puzzle for day20:")
# input20 = get_string_input_array(path="data/day20.txt")
# print(get_count(input20))
# print(get_count_2(input20))

# print("Puzzle for day19:")
# input19 = get_string_input_array(path="data/day19.txt")
# print(get_msg_count(input19))
# print(get_msg_count_2(input19))

# print("Puzzle for day18:")
# input18 = get_string_input_array(path="data/day18.txt")
# print(get_sum_arithmetics(input18))
# print(get_sum_arithmetics(input18, True))

# print("Puzzle for day17:")
# input17 = get_string_input_array(path="data/day17.txt")
# print(get_active_cubes(input17))
# print(get_active_cubes(input17, 2))

# print("Puzzle for day16:")
# input16 = get_string_input_array(path="data/day16.txt")
# print(get_sum_wrong(input16))
# print(get_prod_right(input16, "departure"))


# print("Puzzle for day15:")
# input15 = get_string_input_array(path="data/day15.txt")
# print(get_nth_spoken(input15))
# # print(get_nth_spoken(input15, 30000000))

# print("Puzzle for day14:")
# regmask = r"mask = (.+)"
# regex2 = r"mem\[(\d+)\] = (\d+)"
# input14 = get_string_input_matrix_r_w_offset(
#     path="data/day14.txt", regex=regmask, regex2=regex2
# )
# print(get_memsum(input14))
# print(get_memsum_2(input14))

# print("Puzzle for day13:")
# input13 = get_string_input_array(path="data/day13.txt")
# print(get_bus(input13))
# print(get_bus_2(input13))

# print("Puzzle for day12:")
# regex = r"(\w)(\d*)"
# input12 = get_string_input_matrix_r(path="data/day12.txt", regex=regex)

# print(get_distance(input12))
# print(get_distance_2(input12))


# # print("Puzzle for day11:")
# # input11 = get_string_input_matrix_w_padding(path="data/day11.txt")
# # print(get_seat_count(input11))
# # input11 = get_string_input_matrix_w_padding(path="data/day11.txt")
# # print(get_seat_count_2(input11))

# print("Puzzle for day10:")
# input10 = get_int_input_array(path="data/day10.txt")
# print(get_diff(input10))
# print(get_diff_2(input10))

# print("Puzzle for day9:")
# input9 = get_int_input_array(path="data/day9.txt")
# print(get_first_number(25, input9))
# print(get_list_ends(556543474, input9))

# print("Puzzle for day8:")
# input8 = get_string_input_array(path="data/day8.txt")
# print(get_acc(input8))
# print(get_acc_2(input8))

# print("Puzzle for day7:")
# input7 = get_string_input_array(path="data/day7.txt")
# print(get_bags(input7))
# print(get_bags_2(input7))

# print("Puzzle for day6:")
# input6 = get_string_input_array(path="data/day6.txt")
# print(get_questions_count(input6))
# print(get_questions_everyone_count(input6))

# print("Puzzle for day5:")
# input5 = get_string_input_array(path="data/day5.txt")
# print(get_top_seat(input5))
# print(get_missing_seat(input5))

# print("Puzzle for day4:")
# input4 = get_string_input_array(path="data/day4.txt")
# print(get_valid_passport_count(input4))
# print(get_valid_passport_validation_count(input4))

# print("Puzzle for day3:")
# input3 = get_string_input_array(path="data/day3.txt")
# print(get_tree_count(3, 1, input3))
# all_trees = (
#     get_tree_count(1, 1, input3)
#     * get_tree_count(3, 1, input3)
#     * get_tree_count(5, 1, input3)
#     * get_tree_count(7, 1, input3)
#     * get_tree_count(1, 2, input3)
# )
# print(all_trees)


# print("Puzzle for day2: ")
# input2 = get_string_input_array(path="data/day2.txt")
# print(get_valid_password_count(input2))
# print(get_valid_password_policy2_count(input2))


# print("Puzzle for day1: ")
# numbers1 = get_int_input_array(path="data/day1.txt")
# print(get_product_of_2(numbers1))
# print(get_product_of_3(numbers1))
