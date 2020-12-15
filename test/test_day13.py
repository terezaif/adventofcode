from days.day13 import get_bus
from days.day13 import get_bus_2
from utils.reading_data import get_string_input_array

input = get_string_input_array(path="test/data/day13.txt")


def test_get_bus():
    expected = 295
    actual = get_bus(input)
    assert expected == actual


def test_get_bus_2():
    expected = 1068781
    actual = get_bus_2(input)
    assert expected == actual


def test_get_bus_3():
    input = get_string_input_array(path="test/data/day13_1.txt")
    expected = 1202161486
    actual = get_bus_2(input)
    assert expected == actual
