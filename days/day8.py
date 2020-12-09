# nop +0
# acc +1
# jmp +4
# acc +3
# jmp -3
# acc -99
# acc +1
# jmp -4
# acc +6
import re

operreg = r"(acc|jmp|nop)\s*([+|-])\s*(\d*)"

# This is an infinite loop: with this sequence of jumps, the program will run forever.
# The moment the program tries to run any instruction a second time, you know it will never terminate.

# acc increases or decreases a single global value called the accumulator by the value given in the argument. For example, acc +7 would increase the accumulator by 7. The accumulator starts at 0. After an acc instruction, the instruction immediately below it is executed next.
# jmp jumps to a new instruction relative to itself. The next instruction to execute is found using the argument as an offset from the jmp instruction; for example, jmp +2 would skip the next instruction, jmp +1 would continue to the instruction immediately below it, and jmp -20 would cause the instruction 20 lines above to be executed next.
# nop stands for No OPeration - it does nothing. The instruction immediately below it is executed next.#


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
            # print("loop at", command_line)
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
            # print(commands[i], '->',commands[i])
            acc, not_infinite = get_acc_list(commands)
            # print(acc, not_infinite)
            if not_infinite:
                return acc
            commands[i][0] = "nop"
        elif commands[i][0] == "jmp":
            commands[i][0] = "nop"
            acc, not_infinite = get_acc_list(commands)
            # print(commands[i], '->',commands[i])
            # print(acc, not_infinite)
            if not_infinite:
                return acc
            commands[i][0] = "jmp"
        i += 1
    return acc
