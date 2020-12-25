def parse_input(input):
    p1 = []
    p2 = []
    is_p1 = True
    for line in input:
        if line == "Player 1:" or line == "Player 2:":
            pass
        elif line == "":
            is_p1 = False
        elif is_p1:
            p1.append(int(line))
        else:
            p2.append(int(line))
    return p1, p2


def get_winner(input: list) -> int:
    p1, p2 = parse_input(input)
    while len(p1) > 0 and len(p2) > 0:
        if p1[0] > p2[0]:
            p1.extend([p1[0], p2[0]])
        else:
            p2.extend([p2[0], p1[0]])
        p1.pop(0)
        p2.pop(0)

    w = p1 if p1 != [] else p2

    return sum([c * (len(w) - i) for i, c in enumerate(w)])


def rec_subgame(p1, p2):
    seen_p1 = set()
    seen_p2 = set()

    while len(p1) > 0 and len(p2) > 0:
        if "".join(map(str, p1)) in seen_p1 or "".join(map(str, p2)) in seen_p2:
            break
        if len(p1) > p1[0] and len(p2) > p2[0]:
            a1, a2 = rec_subgame(p1[1 : 1 + p1[0]], p2[1 : 1 + p2[0]])
            if len(a1) > 0:
                p1.extend([p1[0], p2[0]])
            else:
                p2.extend([p2[0], p1[0]])
        elif p1[0] > p2[0]:
            p1.extend([p1[0], p2[0]])
        else:
            p2.extend([p2[0], p1[0]])
        seen_p2.add("".join(map(str, p1)))
        seen_p2.add("".join(map(str, p2)))
        p1.pop(0)
        p2.pop(0)

    return p1, p2


def get_winner_2(input: list) -> int:

    p1, p2 = parse_input(input)
    p1, p2 = rec_subgame(p1, p2)

    w = p1 if p1 != [] else p2

    return sum([c * (len(w) - i) for i, c in enumerate(w)])
