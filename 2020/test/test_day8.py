from days.day8 import get_acc
from days.day8 import get_acc_2
from utils.reading_data import get_string_input_array

input = get_string_input_array(path="2020/test/data/day8.txt")


def test_get_acc():
    expected = 5
    actual = get_acc(input)
    assert expected == actual


def test_get_count_2():
    expected = 8
    actual = get_acc_2(input)
    assert expected == actual
