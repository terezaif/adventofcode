from days.day14 import get_memsum
from days.day14 import get_memsum_2
from utils.reading_data import get_string_input_matrix_r_w_offset

regmask = r"mask = (.+)"
regex2 = r"mem\[(\d+)\] = (\d+)"
input = get_string_input_matrix_r_w_offset(
    path="test/data/day14.txt", regex=regmask, regex2=regex2
)


def test_get_memsum():
    expected = 165
    actual = get_memsum(input)
    assert expected == actual


def test_get_memsum1():
    input = get_string_input_matrix_r_w_offset(
        path="test/data/day14_1.txt", regex=regmask, regex2=regex2
    )
    expected = 165
    actual = get_memsum(input)
    assert expected == actual


def test_get_memsum_2():
    input = get_string_input_matrix_r_w_offset(
        path="test/data/day14_2.txt", regex=regmask, regex2=regex2
    )
    expected = 208
    actual = get_memsum_2(input)
    assert expected == actual
