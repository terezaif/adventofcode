from aocd import get_data


N = [(-1, 0), (-1, 1), (-1, -1)]
S = [(1, 0), (1, 1), (1, -1)]
W = [(0, -1), (1, -1), (-1, -1)]
E = [(0, 1), (1, 1), (-1, 1)]
moves = [N, S, W, E]
allmoves = set(N + S + W + E)


def add(x: tuple, y: tuple) -> tuple:
    return tuple(a + b for a, b in zip(x, y))


def printelves(elves: set, w=5, h=6):
    for j in range(h):
        for i in range(w):
            print("#" if (j, i) in elves else ".", end="")
        print("")


def part1(data, rounds1=10):
    input = [list(s) for s in data.split("\n")]
    w, h = len(input[0]), len(input)
    input = set(
        [
            (j, i)
            for j in range(len(input))
            for i in range(len(input[0]))
            if input[j][i] == "#"
        ]
    )
    elves = input
    E = len(elves)
    # printelves(elves,w,h)
    out = 0
    rounds = 1
    notmoves = []
    while sum(notmoves) != E:
        newmoves = {}
        notmoves = []
        for elf in elves:
            if all([add(elf, m) not in elves for m in allmoves]):
                newmoves[elf] = [elf]
                notmoves.append(True)
            else:
                nm = next(
                    (
                        add(elf, m[0])
                        for m in moves
                        if all([add(elf, p) not in elves for p in m])
                    ),
                    None,
                )
                if nm:
                    ll = newmoves.get(nm, [])
                    ll.append(elf)
                    newmoves[nm] = ll
                else:
                    newmoves[elf] = [elf]

        elves = set()
        for nm, es in newmoves.items():
            if len(es) == 1:
                elves.add(nm)
            else:
                elves |= set(es)
        # print(f"== End of Round {11-rounds} == first move was {moves[0][0]}")
        # printelves(elves,w,h)
        if rounds == rounds1:
            mins = [min([e[i] for e in elves]) for i in range(2)]
            maxs = [max([e[i] for e in elves]) for i in range(2)]
            w, h = maxs[0] - mins[0] + 1, maxs[1] - mins[1] + 1
            # print(w,h, E)
            out = w * h - E
        m = moves.pop(0)
        moves.append(m)
        rounds += 1

    return out, rounds - 1


def part2(data):
    input = [s for s in data.split("\n")]

    return len(input)


def test_part1():
    assert part1(test_data, 10)[0] == 110


def test_part2():
    assert part1(test_data, 10)[1] == 20


data = get_data(day=23, year=2022)

print("spaces, rounds")
print(part1(data, 10))


test_data = """....#..
..###.#
#...#.#
.#...##
#.###..
##.#.##
.#..#.."""
