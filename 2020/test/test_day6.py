from days.day6 import get_questions_count
from days.day6 import get_questions_everyone_count

input = ["abc", "", "a", "b", "c", "", "ab", "ac", "", "a", "a", "a", "a", "", "b"]


def test_get_questions_count():
    expected = 11
    actual = get_questions_count(input)
    assert expected == actual


def test_get_questions_everyone_count():
    expected = 6
    actual = get_questions_everyone_count(input)
    assert expected == actual
