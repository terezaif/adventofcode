from days.day10 import get_diff
from days.day10 import get_diff_2
from utils.reading_data import get_int_input_array


def test_get_diff():
    input = get_int_input_array(path="test/data/day10.txt")
    expected = 35
    actual = get_diff(input)
    assert expected == actual


def test_get_diff_2():
    input = get_int_input_array(path="test/data/day10.txt")
    expected = 8
    actual = get_diff_2(input)
    assert expected == actual


def test_get_diff_2_2():
    input = get_int_input_array(path="test/data/day10_2.txt")
    expected = 19208
    actual = get_diff_2(input)
    assert expected == actual
