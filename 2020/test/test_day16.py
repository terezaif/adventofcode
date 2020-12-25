from days.day16 import get_sum_wrong
from days.day16 import get_prod_right
from utils.reading_data import get_string_input_array

input = get_string_input_array(path="test/data/day16.txt")


def test_get_sum_wrong():
    expected = 71
    actual = get_sum_wrong(input)
    assert expected == actual


def test_get_prod_right():
    input = get_string_input_array(path="test/data/day16_1.txt")
    expected = 12
    actual = get_prod_right(input, starts="class")
    assert expected == actual
