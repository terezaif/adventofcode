import pytest
from days.day17 import get_active_cubes
from utils.reading_data import get_string_input_array, get_string_input_matrix

input = get_string_input_matrix(path="2020/test/data/day17.txt")


def test_get_active_cubes():
    expected = 112
    actual = get_active_cubes(input)
    assert expected == actual


@pytest.mark.skip(reason="takes too long")
def test_get_active_cubes_2():
    expected = 848
    actual = get_active_cubes(input, 2)
    assert expected == actual
