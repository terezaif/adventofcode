import pytest
from days.day24 import get_count
from days.day24 import get_count_2
from utils.reading_data import get_string_input_array

input = get_string_input_array(path="test/data/day24.txt")


def test_get_count():
    expected = 10
    actual = get_count(input)
    assert expected == actual


@pytest.mark.skip(reason="takes too long")
def test_get_count_2():
    expected = 2208
    actual = get_count_2(input)
    assert expected == actual
