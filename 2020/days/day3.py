def get_tree_count(slope_r: int, slope_d: int, input: list) -> int:
    # each row is the element * array length * slope_r
    # on each row we get the element that is
    # at the position : row index * slope_r
    trees = 0
    for depth in range(0, len(input)):
        if depth % slope_d == 0:
            exploded_row = input[depth] * (slope_r * len(input))
            trees += int(exploded_row[(int(depth / slope_d)) * slope_r] == "#")
    return trees
