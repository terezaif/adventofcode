from days.day20 import get_corners

from utils.reading_data import get_string_input_array

input = get_string_input_array(path="test/data/day20.txt")


def test_get_corners():
    expected = 20899048083289
    actual = get_corners(input)
    assert expected == actual
