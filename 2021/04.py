from aocd import get_data
import re


def get_first_last_winning_boards(data):
    input = [s for s in re.split("\n\n|\n", data)]
    numbers = [int(n) for n in input[0].split(",")]
    boards = [re.split("\s+", n.lstrip()) for n in input[1:]]
    winner_boards = set()
    bsize = 5
    draw = 5
    bingo = False
    number_board = 0
    while draw < len(numbers):
        numbers_set = set(numbers[:draw])
        l = 0
        for line in boards:
            s = set([int(n) for n in line])
            if s.issubset(numbers_set):
                number_board = int(l / bsize)
                if bingo == False:
                    winner_boards.add(number_board)
                    number_first_board = number_board
                    number_first_draw = numbers[draw - 1]
                    numbers_first_set = numbers_set
                bingo = True
                if number_board not in winner_boards:
                    number_last_board = number_board
                    number_last_draw = numbers[draw - 1]
                    numbers_last_set = numbers_set
                    winner_boards.add(number_board)
            if l % bsize == 0:  # checking verticals and diagonals
                for v in range(bsize):
                    col = [int(b[v]) for b in boards[l : l + bsize]]
                    s = set([int(b[v]) for b in boards[l : l + bsize]])
                    if s.issubset(numbers_set):
                        number_board = int(l / bsize)
                        if bingo == False:
                            winner_boards.add(number_board)
                            number_first_board = number_board
                            number_first_draw = numbers[draw - 1]
                            numbers_first_set = numbers_set
                        bingo = True
                        if number_board not in winner_boards:
                            number_last_board = number_board
                            number_last_draw = numbers[draw - 1]
                            numbers_last_set = numbers_set
                            winner_boards.add(number_board)
            l += 1
        draw += 1

    # first board
    bingoboard_first = set(
        [
            int(n)
            for li in boards[number_first_board * 5 : number_first_board * 5 + bsize]
            for n in li
        ]
    )
    other_first = list(
        bingoboard_first - bingoboard_first.intersection(numbers_first_set)
    )

    # last board
    bingoboard_last = set(
        [
            int(n)
            for li in boards[number_last_board * 5 : number_last_board * 5 + bsize]
            for n in li
        ]
    )
    other_last = list(bingoboard_last - bingoboard_last.intersection(numbers_last_set))

    return number_first_draw * sum(other_first), number_last_draw * sum(other_last)


def part1(data):
    return get_first_last_winning_boards(data)[0]


def part2(data):
    return get_first_last_winning_boards(data)[1]


def test_part1():
    assert part1(test_data) == 4512


def test_part2():
    assert part2(test_data) == 1924


data = get_data(day=4, year=2021)

print(part1(data))
print(part2(data))

test_data = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7"""
