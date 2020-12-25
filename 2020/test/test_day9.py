from days.day9 import get_first_number
from days.day9 import get_list_ends
from utils.reading_data import get_int_input_array

input = get_int_input_array(path="test/data/day9.txt")


def test_get_count():
    expected = 127
    actual = get_first_number(5, input)
    assert expected == actual


def test_get_count_2():
    expected = 62
    actual = get_list_ends(127, input)
    assert expected == actual
