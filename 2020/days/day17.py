def get_tuples(input: list, dim: int = 1):
    active = set()
    inactive = set()
    for i in range(0, len(input)):
        for j in range(0, len(input[i])):
            t = tuple([i, j] + [0] * dim)
            if input[i][j] == "#":
                active.add(t)
            else:
                inactive.add(t)
    return active, inactive


def get_active_cubes(input: list, extradim: int = 1) -> int:
    active, inactive = get_tuples(input, extradim)
    steps = 6
    while steps > 0:
        active, inactive = shuffle(active, inactive, extradim)
        steps += -1

    return len(active)


def shuffle(active, inactive, dim: int = 3):
    new_active = set()
    new_inactive = set()
    neighbors = set()
    for t in active:
        n = get_neighbors_3(t, dim)
        s = n.intersection(active)
        n_s = n - s
        if len(s) in [2, 3]:
            new_active.add(t)
        else:
            new_inactive.add(t)
        neighbors.update(n_s)
    for t in inactive:
        n = get_neighbors_3(t, dim)
        s = n.intersection(active)
        n_s = n - s
        if len(s) in [3]:
            new_active.add(t)
        else:
            new_inactive.add(t)
        neighbors.update(n_s)
    for t in neighbors:
        n = get_neighbors_3(t, dim)
        s = n.intersection(active)
        n_s = n - s
        if len(s) in [3]:
            new_active.add(t)
        else:
            new_inactive.add(t)
    return new_active, new_inactive


def get_neighbors_3(t, edim: int = 1):
    if edim == 1:
        n = [
            (i, j, k)
            for i in range(t[0] - 1, t[0] + 2)
            for j in range(t[1] - 1, t[1] + 2)
            for k in range(t[2] - 1, t[2] + 2)
        ]
        s = set(n)
        s.remove(t)
    elif edim == 2:
        n = [
            (i, j, k, l)
            for i in range(t[0] - 1, t[0] + 2)
            for j in range(t[1] - 1, t[1] + 2)
            for k in range(t[2] - 1, t[2] + 2)
            for l in range(t[3] - 1, t[3] + 2)
        ]
        s = set(n)
        s.remove(t)
    return s
