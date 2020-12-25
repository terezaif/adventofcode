from days.day21 import get_goodfood_count
from days.day21 import get_badfood
from utils.reading_data import get_string_input_array

input = get_string_input_array(path="test/data/day21.txt")


def test_get_goodfood_count():
    expected = 5
    actual = get_goodfood_count(input)
    assert expected == actual


def test_get_badfood():
    expected = "mxmxvkd,sqjhc,fvjkl"
    actual = get_badfood(input)
    assert expected == actual
