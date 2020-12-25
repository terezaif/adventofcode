from days.day25 import get_handshake
from utils.reading_data import get_string_input_array

input = get_string_input_array(path="test/data/day25.txt")


def test_get_handshake():
    expected = 14897079
    actual = get_handshake(input)
    assert expected == actual
