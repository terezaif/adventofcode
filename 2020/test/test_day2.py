from days.day2 import (
    is_password_valid,
    get_valid_password_count,
    is_password_valid_policy2,
)

# import days.day2


def test_is_password_valid_false():
    data = "1-3 b: cdefg"
    expected = False
    actual = is_password_valid(data)
    assert expected == actual


def test_is_password_valid_true():
    data = "1-3 a: abcde"
    expected = True
    actual = is_password_valid(data)
    assert expected == actual


def test_is_password_valid_policy2_true():
    data = "1-3 a: abcde"
    expected = True
    actual = is_password_valid_policy2(data)
    assert expected == actual


def test_is_password_valid_policy2_false():
    data = "1-3 b: cdefg"
    expected = False
    actual = is_password_valid_policy2(data)
    assert expected == actual


def test_is_password_valid_policy2_false_both():
    data = "2-9 c: ccccccccc"
    expected = False
    actual = is_password_valid_policy2(data)
    assert expected == actual


def test_get_valid_password_count_correct():
    test_input = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]
    expected = 2
    actual = get_valid_password_count(test_input)
    assert expected == actual
