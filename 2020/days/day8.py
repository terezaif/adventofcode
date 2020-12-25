import re

operreg = r"(acc|jmp|nop)\s*([+|-])\s*(\d*)"


def get_acc(input: list) -> int:
    commands = [list(re.findall(operreg, line)[0]) for line in input]

    acc, not_infinite = get_acc_list(commands)
    return acc


ops = {"+": (lambda x, y: x + y), "-": (lambda x, y: x - y)}


def get_acc_list(commands: list) -> (int, bool):
    acc = 0
    visited = set()
    not_infinite = True
    command_line = 0
    while command_line < len(commands):
        if command_line in visited:
            not_infinite = False
            return acc, not_infinite
        visited.add(command_line)
        co = commands[command_line]
        if co[0] == "nop":
            command_line += 1
        elif co[0] == "acc":
            acc = ops[co[1]](acc, int(co[2]))
            command_line += 1
        elif co[0] == "jmp":
            command_line = ops[co[1]](command_line, int(co[2]))

    return acc, not_infinite


def get_acc_2(input: list) -> int:
    commands = [list(re.findall(operreg, line)[0]) for line in input]
    print(get_acc_list(commands))
    acc = 0
    i = 0
    for i in range(0, len(commands)):
        if commands[i][0] == "nop":
            commands[i][0] = "jmp"
            acc, not_infinite = get_acc_list(commands)
            if not_infinite:
                return acc
            commands[i][0] = "nop"
        elif commands[i][0] == "jmp":
            commands[i][0] = "nop"
            acc, not_infinite = get_acc_list(commands)
            if not_infinite:
                return acc
            commands[i][0] = "jmp"
        i += 1
    return acc
