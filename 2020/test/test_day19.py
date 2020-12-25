from days.day19 import get_msg_count
from days.day19 import get_msg_count_2
from utils.reading_data import get_string_input_array

input = get_string_input_array(path="test/data/day19_1.txt")


def test_get_count():
    expected = 8
    actual = get_msg_count(input)
    assert expected == actual


def test_get_count_1():
    input = get_string_input_array(path="test/data/day19.txt")
    expected = 2
    actual = get_msg_count(input)
    assert expected == actual


def test_get_count_2():
    input = get_string_input_array(path="test/data/day19_2.txt")
    expected = 3
    actual = get_msg_count(input)
    assert expected == actual


def test_get_count_2_1():
    input = get_string_input_array(path="test/data/day19_2.txt")
    expected = 12
    actual = get_msg_count_2(input)
    assert expected == actual
