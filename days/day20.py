from parse import parse
import operator
import math


def get_tiles(input):
    tiles = {}
    tile_id = None
    for line in input:
        p = parse("Tile {:d}:", line)
        if p:
            tile_id = p[0]
            piece = []
        elif line != "":
            piece.append(list(line))
        else:
            tiles[tile_id] = piece
    tiles[tile_id] = piece

    return tiles


def get_corners(input: list) -> int:
    tiles = get_tiles(input)
    print(tiles.keys())
    tedges, edges = get_edges(tiles)
    count_one, count_two, tones_singles = get_single_edges_tiles(edges)
    print(tones_singles)
    corners = get_grid(tedges, edges)
    return math.prod(corners)


def get_grid(tedges, edges):
    top = []
    right = []
    bot = []
    left = []
    mid = []
    corner = []
    not_fitting = []
    for t, ed in tedges.items():
        matching = [int((len(edges.get(ed[i], []))) == 2) for i in range(0, 4)]
        if matching == [0, 1, 1, 1]:
            top.append(t)
        elif matching == [1, 0, 1, 1]:
            right.append(t)
        elif matching == [1, 1, 0, 1]:
            bot.append(t)
        elif matching == [1, 1, 1, 0]:
            left.append(t)
        elif matching == [1, 1, 1, 1]:
            mid.append(t)
        elif matching in [[0, 0, 1, 1], [1, 0, 0, 1], [1, 1, 0, 0], [0, 1, 1, 0]]:
            corner.append(t)
        else:
            not_fitting.append(t)

    print("top: ", len(top), sorted(top))
    print("right: ", len(right), sorted(right))
    print("bot: ", len(bot), sorted(bot))
    print("left: ", len(left), sorted(left))
    print("mid: ", len(mid), sorted(mid))
    print("corner: ", len(corner), sorted(corner))
    print("not_fitting: ", len(not_fitting), sorted(not_fitting))

    return corner


def get_single_edges_tiles(edges):
    count_one = 0
    count_two = 0
    tones_singles = {}
    for e, ts in edges.items():
        count_one += 1 if len(ts) == 1 else 0
        count_two += 1 if len(ts) == 2 else 0
        if (len(ts)) == 1:
            tid = next(iter(ts))
            tones_singles[tid] = tones_singles.get(tid, 0) + 1
    return count_one, count_two, tones_singles


# [::-1]


def get_edges(tiles):
    tedges = {}
    edges = {}
    for id, tile in tiles.items():
        w = len(tile[0])
        h = len(tile)
        e1 = "".join(tile[0])
        e2 = "".join([item[0] for item in tile])
        e3 = "".join(tile[h - 1])
        e4 = "".join([item[w - 1] for item in tile])

        tedges[id] = [e1, e2, e3, e4]
        edges.setdefault(e1, set()).add(id)
        edges.setdefault(e3, set()).add(id)
        edges.setdefault(e2, set()).add(id)
        edges.setdefault(e4, set()).add(id)
        edges.setdefault(e1[::-1], set()).add(id)
        edges.setdefault(e3[::-1], set()).add(id)
        edges.setdefault(e2[::-1], set()).add(id)
        edges.setdefault(e4[::-1], set()).add(id)
    return tedges, edges


def get_count_2(input: list) -> int:
    return 10
