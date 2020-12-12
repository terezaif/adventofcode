compas = {"S": [0, -1], "N": [0, 1], "E": [1, 0], "W": [-1, 0]}


def get_multiplied_vector(array, scalar):
    return [element * scalar for element in array]


def get_add_vectors(first, second):
    return [x + y for x, y in zip(first, second)]


def rotate(unit, dir, angle):
    if angle == "180":
        return [unit[0] * -1, unit[1] * -1]
    elif dir + angle in ["L270", "R90"]:
        return [unit[1], unit[0] * -1]
    elif dir + angle in ["R270", "L90"]:
        return [unit[1] * -1, unit[0]]


def get_distance(input: list) -> int:
    start = [0, 0]
    direction = [1, 0]  # "E"
    for ins, stride in input:
        if ins in ["R", "L"]:
            # print(direction, ins, stride, start)
            direction = rotate(direction, ins, stride)
        elif ins == "F":
            start = get_add_vectors(
                start, get_multiplied_vector(direction, int(stride))
            )
        else:
            unit = compas[ins]
            start = get_add_vectors(start, get_multiplied_vector(unit, int(stride)))

    return abs(start[0]) + abs(start[1])


def get_distance_2(input: list) -> int:
    start = [0, 0]
    waypoint = [10, 1]
    for ins, stride in input:
        if ins in ["R", "L"]:
            waypoint = rotate(waypoint, ins, stride)
        elif ins == "F":
            start = get_add_vectors(start, get_multiplied_vector(waypoint, int(stride)))
        else:
            unit = compas[ins]
            waypoint = get_add_vectors(
                waypoint, get_multiplied_vector(unit, int(stride))
            )

    return abs(start[0]) + abs(start[1])
