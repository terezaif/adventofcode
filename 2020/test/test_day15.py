import pytest
from days.day15 import get_nth_spoken
from utils.reading_data import get_string_input_array

input = get_string_input_array(path="2020/test/data/day15.txt")


def test_get_nth_spoken():
    expected = 436
    actual = get_nth_spoken(input)
    assert expected == actual


@pytest.mark.skip(reason="takes too long")
def test_get_nth_spoken_2():
    expected = 175594
    actual = get_nth_spoken(input, 30000000)
    assert expected == actual
