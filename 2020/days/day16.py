from parse import parse
import math


def get_sum_wrong(input: list) -> int:
    rules, your_ticket, nearby_tickets = get_rules_and_tickets(input)
    inv = sum([check_ticket_any(rules, ticket) for ticket in nearby_tickets])
    return inv


def get_prod_right(input: list, starts: str) -> int:
    rules, your_ticket, nearby_tickets = get_rules_and_tickets(input)
    valid_tickets = [
        ticket for ticket in nearby_tickets if check_ticket_correct(rules, ticket)
    ]
    rules_pos = {}
    postions = len(your_ticket)
    for p in range(0, postions):
        for r in rules:
            if all(
                [
                    (
                        (r[1] <= valid_tickets[j][p] <= r[2])
                        | (r[3] <= valid_tickets[j][p] <= r[4])
                    )
                    for j in range(0, len(valid_tickets))
                ]
            ):
                rules_pos.setdefault(r[0], []).append(p)

    pos_w_start = []
    while rules_pos != {}:
        r, p = next((k, v[0]) for k, v in rules_pos.items() if len(v) == 1)
        if r.startswith(starts):
            pos_w_start.append(p)
        rules_pos.pop(r)
        for k, v in rules_pos.items():
            if p in v:
                rules_pos[k].remove(p)
    starts_prod = math.prod([your_ticket[i] for i in pos_w_start])

    return starts_prod


def check_ticket_any(rules, ticket):
    wrong = [
        n
        for n in ticket
        if not any([((r[1] <= n <= r[2]) | (r[3] <= n <= r[4])) for r in rules])
    ]
    return sum(wrong)


def check_ticket_correct(rules, ticket):
    wrong = [
        n
        for n in ticket
        if not any([((r[1] <= n <= r[2]) | (r[3] <= n <= r[4])) for r in rules])
    ]
    return len(wrong) == 0


def get_rules_and_tickets(input: list):
    rules = []
    your_ticket = []
    nearby_tickets = []
    inputtype = "r"
    for line in input:
        if line == "":
            pass
        elif line == "your ticket:":
            inputtype = "y"
        elif line == "nearby tickets:":
            inputtype = "n"
        elif inputtype == "r":
            p = parse("{}: {:d}-{:d} or {:d}-{:d}", line)
            rules.append([p[0], p[1], p[2], p[3], p[4]])
        elif inputtype == "y":
            your_ticket = [int(l) for l in line.split(",")]
        elif inputtype == "n":
            nearby_tickets.append([int(l) for l in line.split(",")])
    return rules, your_ticket, nearby_tickets
