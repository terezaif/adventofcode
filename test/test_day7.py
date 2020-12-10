import pytest
from days.day7 import get_bags
from days.day7 import get_bags_2
from utils.reading_data import get_string_input_array

input = [
    "light red bags contain 1 bright white bag, 2 muted yellow bags.",
    "dark orange bags contain 3 bright white bags, 4 muted yellow bags.",
    "bright white bags contain 1 shiny gold bag.",
    "muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.",
    "shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.",
    "dark olive bags contain 3 faded blue bags, 4 dotted black bags.",
    "vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.",
    "faded blue bags contain no other bags.",
    "dotted black bags contain no other bags.",
]
input2 = [
    "shiny gold bags contain 2 dark red bags.",
    "dark red bags contain 2 dark orange bags.",
    "dark orange bags contain 2 dark yellow bags.",
    "dark yellow bags contain 2 dark green bags.",
    "dark green bags contain 2 dark blue bags.",
    "dark blue bags contain 2 dark violet bags.",
    "dark violet bags contain no other bags.",
]
input3 = get_string_input_array(path="test/data/day7.txt")


def test_get_count():
    expected = 4
    actual = get_bags(input)
    assert expected == actual


def test_get_count_2():
    expected = 32
    actual = get_bags_2(input)
    assert expected == actual


def test_get_count_2_2():
    expected = 126
    actual = get_bags_2(input2)
    assert expected == actual


@pytest.mark.skip(reason="cannot work")
def test_get_count_2_t():
    expected = 1151
    actual = get_bags_2(input3)
    assert expected == actual
