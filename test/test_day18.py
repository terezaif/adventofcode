from days.day18 import get_sum_arithmetics
from utils.reading_data import get_string_input_array

input = get_string_input_array(path="test/data/day18.txt")


def test_get_sum_arithmetics():
    expected = 71
    actual = get_sum_arithmetics(input)
    assert expected == actual


def test_get_sum_arithmetics_2():
    input = get_string_input_array(path="test/data/day18_1.txt")
    expected = 51
    actual = get_sum_arithmetics(input)
    assert expected == actual


def test_get_sum_arithmetics_3():
    input = get_string_input_array(path="test/data/day18_2.txt")
    expected = 26 + 437 + 12240 + 13632
    actual = get_sum_arithmetics(input)
    assert expected == actual


def test_get_sum_arithmetics_0_2():
    expected = 231
    actual = get_sum_arithmetics(input, True)
    assert expected == actual


def test_get_sum_arithmetics_2_2():
    input = get_string_input_array(path="test/data/day18_1.txt")
    expected = 51
    actual = get_sum_arithmetics(input, True)
    assert expected == actual


def test_get_sum_arithmetics_2_3():
    input = get_string_input_array(path="test/data/day18_2.txt")
    expected = 46 + 1445 + 669060 + 23340
    actual = get_sum_arithmetics(input, True)
    assert expected == actual
