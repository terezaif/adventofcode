from aocd import get_data


def part1(data):
    prev = {}
    sizes = {}
    dir = "/"
    sizes[dir] = 0
    for line in data.split("\n")[1:]:
        match line.split(" "):
            case ["$", "cd", dirname]:
                match dirname:
                    case "..":
                        sizes[prev[dir]] = sizes[prev[dir]] + sizes[dir]
                        dir = prev[dir]
                    case _:
                        dir = dir + dirname + "/"
            case ["$", "ls"]:
                sizes[dir] = 0
            case [a, b]:
                match a:
                    case "dir":
                        prev[dir + b + "/"] = dir
                    case _:
                        sizes[dir] = sizes[dir] + int(a)
    while dir != "/":
        sizes[prev[dir]] = sizes[prev[dir]] + sizes[dir]
        dir = prev[dir]
    return sum([v for v in sizes.values() if v <= 100000]), sizes


def part2(data):
    dirfilesize = part1(data)[1]

    total = 70000000
    need = 30000000
    free = total - dirfilesize["/"]

    return min([v for v in dirfilesize.values() if v >= need - free])


def test_part1():
    assert part1(test_data)[0] == 95437


def test_part2():
    assert part2(test_data) == 24933642


data = get_data(day=7, year=2022)

print(part1(data)[0])
print(part2(data))

test_data = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""
