from tqdm import tqdm


def parse_input(input):
    circle = [int(c) - 1 for c in input[0]]
    sc = sorted(circle, reverse=True)
    return circle, sc


def parse_input_2(input, max: int = 1000000):
    circle = [int(c) - 1 for c in input[0]]
    rest = [i for i in range(9, max)]
    circle = circle + rest
    sc = sorted(circle, reverse=True)
    return circle, sc


def run_game(circle, sc, moves):

    cur = circle[0]
    # one = circle.index(1)
    # circle = circle[one:] + circle[:one]
    # initial = circle[:]
    m = max(circle) + 1
    size = len(circle)

    # dsc = sc + sc
    for move in tqdm(range(moves)):
        cur = circle.pop(0)
        p3 = [circle.pop(0) for i in range(0, 3)]

        n = next(
            ((cur - k + m) % m for k in range(1, 5) if (cur - k + m) % m not in p3)
        )
        # d = next(index for index, value in enumerate(circle) if value == n)
        d = next(size - 5 - i for i in range(0, size - 4) if circle[size - 5 - i] == n)
        # d = circle.index(n)
        # print(d)
        # print(d)

        circle[d + 1 : d + 1] = p3
        circle.append(cur)

        # one = circle.index(1)
        # circle = circle[one:] + circle[:one]
        # i = circle.index(cur)
        # i = (i+1)%size
        # moves -= 1
        # if(circle == initial):
        # 	print("pattern repeating at: moves=",moves)

    one = circle.index(1)
    circle = circle[one:] + circle[:one]
    return circle


def get_seq(input: list, moves: int = 100) -> int:
    circle, sc = parse_input(input)

    circle = run_game(circle, sc, moves)

    circle = [i + 1 for i in circle]
    one = circle.index(1)
    return int("".join(map(str, circle[one + 1 :])) + "".join(map(str, circle[:one])))


def get_count_2(input: list, moves: int = 1000000, max: int = 1000000) -> int:
    circle, sc = parse_input_2(input, max)

    circle = run_game(circle, sc, moves)
    one = circle.index(0)
    cup1 = circle[one + 1] + 1
    cup2 = circle[one + 2] + 1
    return cup1 * cup2
