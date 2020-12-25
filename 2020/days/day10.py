# Any given adapter can take an
# input 1, 2, or 3 jolts lower than its
# rating and still produce its rated output joltage
# In addition, your device has a built-in
# joltage adapter rated for 3 jolts higher
# than the highest-rated adapter in your bag.
# (If your adapter list were 3, 9, and 6,
# your device's built-in adapter would be rated for 12 jolts.)
import math

allowed = [1, 2, 3]
extra = 3
default = 0


def get_diff(input: list) -> int:
    yours = max(input) + extra
    input.append(default)
    input.append(yours)
    input.sort()

    diff = [a_i - b_i for a_i, b_i in zip(input[1:], input[: len(input) - 1])]
    return diff.count(3) * diff.count(1)


def get_diff_2(input: list) -> int:
    yours = max(input) + extra
    input.append(default)
    input.append(yours)
    input.sort()
    diff = [a_i - b_i for a_i, b_i in zip(input[1:], input[: len(input)])]
    permutations = get_ones_lists(diff[: len(diff)])
    fact = [get_permutation_count(x) for x in permutations]
    return math.prod(fact)


def get_ones_lists(numbers):
    counts = []
    c = 0
    for n in numbers:
        if n == 1:
            c += 1
        if n != 1:
            if c != 0:
                counts.append(c - 1)
                c = 0
    return counts


def get_permutation_count(n):
    if n == 0:
        return 1
    if n == 1:
        return pow(2, n)
    if n == 2:
        return pow(2, n)
    else:
        return pow(2, 3) - 1
