import pytest
from days.day23 import get_seq
from days.day23 import get_count_2
from utils.reading_data import get_string_input_array

input = get_string_input_array(path="2020/test/data/day23.txt")


def test_get_count_10():
    expected = 92658374
    actual = get_seq(input, 10)
    assert expected == actual


def test_get_count():
    expected = 67384529
    actual = get_seq(input)
    assert expected == actual


@pytest.mark.skip(reason="takes too long")
def test_get_count_2():
    expected = 149245887792
    actual = get_count_2(input, 100, 10**6)
    assert expected == actual
