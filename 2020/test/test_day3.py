from days.day3 import get_tree_count

input = [
    "..##.......",
    "#...#...#..",
    ".#....#..#.",
    "..#.#...#.#",
    ".#...##..#.",
    "..#.##.....",
    ".#.#.#....#",
    ".#........#",
    "#.##...#...",
    "#...##....#",
    ".#..#...#.#",
]


def test_get_tree_count_r1_d1():
    expected = 2
    actual = get_tree_count(1, 1, input)
    assert actual == expected


def test_get_tree_count_r3_d1():
    expected = 7
    actual = get_tree_count(3, 1, input)
    assert actual == expected


def test_get_tree_count_r5_d1():
    expected = 3
    actual = get_tree_count(5, 1, input)
    assert actual == expected


def test_get_tree_count_r7_d1():
    expected = 4
    actual = get_tree_count(7, 1, input)
    assert actual == expected


def test_get_tree_count_r1_d2():
    expected = 2
    actual = get_tree_count(1, 2, input)
    assert actual == expected
