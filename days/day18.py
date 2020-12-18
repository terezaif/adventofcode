import re


def get_sum_arithmetics(input: list, plus_first: bool = False) -> int:
    o = []
    for line in input:
        line = line.replace("(", "( ")
        line = line.replace(")", " )")
        line = line.replace(" ", " ")
        m = line.split(" ")
        while len(m) > 1:
            m = run_ops(m, plus_first)
        o.append(int(m[0]))
    return sum(o)


def run_ops(ms: list, plus_first: bool = False):
    p_ind = next((ind for ind, e in enumerate(ms) if e == "("), False)
    if p_ind is False:
        ms = run_simple_ops(ms, plus_first)
    else:
        i, j, n = find_first_complete_p(ms, plus_first)
        ms[i : j + 1] = n
    return ms


def find_first_complete_p(ms: list, plus_first: bool = False):
    i = 0
    for ind, e in enumerate(ms):
        if e == "(":
            i = ind
        if e == ")":
            j = ind
            break
    res = run_simple_ops(ms[i + 1 : j], plus_first)
    return i, j, res


def run_simple_ops(ms: list, plus_first: bool = False):
    if plus_first is False:
        while len(ms) > 1:
            o = ops[ms[1]](int(ms[0]), int(ms[2]))
            ms[0:3] = [o]
    else:
        while len(ms) > 1:
            p_ind = next((ind for ind, e in enumerate(ms) if e == "+"), False)
            if p_ind is not False:
                o = ops[ms[p_ind]](int(ms[p_ind - 1]), int(ms[p_ind + 1]))
                ms[p_ind - 1 : p_ind + 2] = [o]
            else:
                o = ops[ms[1]](int(ms[0]), int(ms[2]))
                ms[0:3] = [o]
    return ms


ops = {"+": (lambda x, y: x + y), "*": (lambda x, y: x * y)}
