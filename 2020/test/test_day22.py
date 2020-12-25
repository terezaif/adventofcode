from days.day22 import get_winner
from days.day22 import get_winner_2
from utils.reading_data import get_string_input_array

input = get_string_input_array(path="2020/test/data/day22.txt")


def test_get_winner():
    expected = 306
    actual = get_winner(input)
    assert expected == actual


def test_get_winner_2():
    expected = 291
    actual = get_winner_2(input)
    assert expected == actual
