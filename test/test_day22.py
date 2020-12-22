from days.day22 import get_count
from days.day22 import get_count_2
from utils.reading_data import get_string_input_array

input = get_string_input_array(path="test/data/day22.txt")


def test_get_count():
    expected = 306
    actual = get_count(input)
    assert expected == actual


def test_get_count_2():
    expected = 291
    actual = get_count_2(input)
    assert expected == actual
