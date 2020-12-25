from days.day5 import get_seat_id, get_top_seat


def test_get_seat_id_1():
    input = "FBFBBFFRLR"
    expected = 357
    actual = get_seat_id(input)
    assert expected == actual


def test_get_seat_id_2():
    input = "BFFFBBFRRR"
    expected = 567
    actual = get_seat_id(input)
    assert expected == actual


def test_get_seat_id_3():
    input = "FFFBBBFRRR"
    expected = 119
    actual = get_seat_id(input)
    assert expected == actual


def test_get_seat_id_4():
    input = "BBFFBBFRLL"
    expected = 820
    actual = get_seat_id(input)
    assert expected == actual


def test_get_top_seat():
    input = ["BFFFBBFRRR", "FFFBBBFRRR", "BBFFBBFRLL"]
    expected = 820
    actual = get_top_seat(input)
    assert actual == expected
