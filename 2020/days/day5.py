ROW_COUNT = 128
COLUMN_COUNT = 8


def get_seat_id(input: str) -> int:
    # FBFBBFFRLR
    # range is 0- 127
    operations = list(input)
    front = 0
    back = ROW_COUNT - 1
    left = 0
    right = COLUMN_COUNT - 1
    for operation in operations:
        if operation == "F":
            back = int((back - front) / 2) + front
        if operation == "B":
            front = int((back - front) / 2) + 1 + front
        if operation == "L":
            right = int((right - left) / 2) + left
        if operation == "R":
            left = int((right - left) / 2) + 1 + left
    return front * COLUMN_COUNT + left


def get_top_seat(input: list) -> int:
    max = 0
    for operations in input:
        seat = get_seat_id(operations)
        if seat > max:
            max = seat
    return max


def get_missing_seat(input: list) -> int:
    max = 0
    min = ROW_COUNT * COLUMN_COUNT
    seat_least = []
    for operations in input:
        seat = get_seat_id(operations)
        if seat > max:
            max = seat
        if seat < min:
            min = seat
        seat_least.append(seat)
    range_seats = range(min, max + 1)
    return list(set(range_seats) - set(seat_least))[0]
