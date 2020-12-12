from days.day11 import get_seat_count
from days.day11 import get_seat_count_2
from utils.reading_data import (
    get_string_input_matrix_w_padding,
    get_string_input_matrix,
)


def test_get_seat_count():
    input = get_string_input_matrix_w_padding(path="test/data/day11.txt")
    expected = 37
    actual = get_seat_count(input)
    assert expected == actual


def test_get_seat_count_2():
    input = get_string_input_matrix(path="test/data/day11.txt")
    expected = 26
    actual = get_seat_count_2(input)
    assert expected == actual
