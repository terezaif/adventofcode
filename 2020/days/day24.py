from functools import reduce
from tqdm import tqdm

changers = {"n", "s"}
singles = {"e", "w"}

dirs = {
    "ne": [1, 1],
    "sw": [-1, -1],
    "nw": [0, 1],
    "se": [0, -1],
    "e": [1, 0],
    "w": [-1, 0],
}


def parse_input(input: list):
    tiles = []
    tiles_3 = []
    for t in input:
        # print(t)
        coords = []
        coords_3 = []
        prev = None
        for c in t:
            if prev is None:
                if c in singles:
                    coords.append(dirs[c])
                else:
                    prev = c
            else:
                if c in singles:
                    coords.append(dirs[prev + c])
                    prev = None
                else:
                    coords.append(dirs[prev])
                    prev = c
        if prev is not None:
            coords.append(dirs[prev])
        tiles.append(coords)
        tiles_3.append(coords_3)
    return tiles, tiles_3


def add_vectors(first, second):
    return [x + y for x, y in zip(first, second)]


def get_count(input: list) -> int:
    tiles, tiles_3 = parse_input(input)
    ts = {}
    for i, t in enumerate(tiles):
        coords = tuple(reduce(add_vectors, t))
        ts[coords] = ts.setdefault(coords, 0) + 1
    return len([k for k, v in ts.items() if v % 2 != 0])


def get_count_2(input: list) -> int:
    tiles, titles_3 = parse_input(input)
    ts = {}
    for t in tiles:
        coords = tuple(reduce(add_vectors, t))
        ts[coords] = ts.setdefault(coords, 0) + 1

    black = set([k for k, v in ts.items() if v % 2 != 0])
    white = set([k for k, v in ts.items() if v % 2 == 0])

    days = 100
    for i in tqdm(range(days)):
        black, white = shuffle(black, white)
    return len(black)


def shuffle(black, white):
    nb = set()
    nw = set()
    for b in black:
        ne = get_neighbors(b)
        bne = ne.intersection(black)
        if len(bne) == 0 or len(bne) > 2:
            nw.add(b)
        else:
            nb.add(b)
        wne = ne - bne
        white |= wne
    for w in white:
        ne = get_neighbors(w)
        bne = ne.intersection(black)
        if len(bne) == 2:
            nb.add(w)
        else:
            nw.add(w)
        wne = ne - bne
        nw |= wne
    return nb, nw


def get_neighbors(t: tuple):
    neighbours = set([tuple(add_vectors(t, d)) for k, d in dirs.items()])
    return neighbours
