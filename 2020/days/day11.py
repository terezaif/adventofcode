import copy


def get_seat_count(input: list) -> int:
    changes, input = shuffle_seats(input)
    while changes > 0:
        changes, input = shuffle_seats(input)
    return get_seats(input)


def shuffle_seats(input):
    new_state = copy.deepcopy(input)
    changes = 0
    for r in range(0, len(input)):
        for c in range(0, len(input[r])):
            if input[r][c] == "L" and get_neighbors_occupied(r, c, input) == 0:
                new_state[r][c] = "#"
                changes += 1
            elif input[r][c] == "#" and get_neighbors_occupied(r, c, input) >= 5:
                new_state[r][c] = "L"
                changes += 1
    return changes, new_state


def get_neighbors_occupied(r, c, input):
    occupied = sum(
        [input[i][j] == "#" for i in range(r - 1, r + 2) for j in range(c - 1, c + 2)]
    )
    return occupied


def print_array(input):
    for line in input:
        print("".join(line))


def get_seat_count_2(input: list) -> int:
    # print(get_seats(input))
    # print_array(input)
    changes, input = shuffle_seats_diagonal(input)
    # print_array(input)
    # print(get_seats(input))
    while changes > 0:
        changes, input = shuffle_seats_diagonal(input)
        # print_array(input)
        # print(get_seats(input))

    return get_seats(input)


def shuffle_seats_diagonal(input):
    new_state = copy.deepcopy(input)
    changes = 0
    for r in range(0, len(input)):
        for c in range(0, len(input[r])):
            if input[r][c] == "L" and get_neighbors_occupied_diagonal(r, c, input) == 0:
                new_state[r][c] = "#"
                changes += 1
            elif (
                input[r][c] == "#" and get_neighbors_occupied_diagonal(r, c, input) >= 5
            ):
                new_state[r][c] = "L"
                changes += 1
    return changes, new_state


def get_neighbors_occupied_diagonal(r, c, input):
    mr = len(input)
    mc = len(input[0])
    dirs = []

    dirs.append(
        next(
            (
                input[r - incr][c + incr] == "#"
                for incr in range(1, min(r + 1, mc - c))
                if input[r - incr][c + incr] in ["L", "#"]
            ),
            False,
        )
    )  # top left
    dirs.append(
        next(
            (
                input[r + incr][c + incr] == "#"
                for incr in range(1, min(mr - r, mc - c))
                if input[r + incr][c + incr] in ["L", "#"]
            ),
            False,
        )
    )  # bot left
    dirs.append(
        next(
            (
                input[r + incr][c - incr] == "#"
                for incr in range(1, min(mr - r, c + 1))
                if input[r + incr][c - incr] in ["L", "#"]
            ),
            False,
        )
    )  # bot right
    dirs.append(
        next(
            (
                input[r - incr][c - incr] == "#"
                for incr in range(1, min(r + 1, c + 1))
                if input[r - incr][c - incr] in ["L", "#"]
            ),
            False,
        )
    )  # top right

    dirs.append(
        next(
            (
                input[r][c + incr] == "#"
                for incr in range(1, mc - c)
                if input[r][c + incr] in ["L", "#"]
            ),
            False,
        )
    )
    dirs.append(
        next(
            (
                input[r][c - incr] == "#"
                for incr in range(1, c + 1)
                if input[r][c - incr] in ["L", "#"]
            ),
            False,
        )
    )
    dirs.append(
        next(
            (
                input[r + incr][c] == "#"
                for incr in range(1, mr - r)
                if input[r + incr][c] in ["L", "#"]
            ),
            False,
        )
    )
    dirs.append(
        next(
            (
                input[r - incr][c] == "#"
                for incr in range(1, r + 1)
                if input[r - incr][c] in ["L", "#"]
            ),
            False,
        )
    )
    occupied = sum(dirs)
    return occupied


def get_seats(matrix):
    seats = sum(
        [
            matrix[i][j] == "#"
            for i in range(0, len(matrix))
            for j in range(0, len(matrix))
        ]
    )
    return seats
