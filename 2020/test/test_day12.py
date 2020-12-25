from days.day12 import get_distance
from days.day12 import get_distance_2
from utils.reading_data import get_string_input_matrix_r


regex = r"(\w)(\d*)"
input = get_string_input_matrix_r(path="test/data/day12.txt", regex=regex)


def test_get_distance():
    expected = 25
    actual = get_distance(input)
    assert expected == actual


def test_get_distance_2():
    expected = 286
    actual = get_distance_2(input)
    assert expected == actual
