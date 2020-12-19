from parse import parse


def get_rules_messages(input):
    rules = {}
    rules_end = {}
    rules_or = {}
    messages = []
    sp = input.index("")
    for r in input[:sp]:
        pe = parse('{}: "{:w}"', r)
        po = parse("{}: {} | {}", r)
        p = parse("{}: {}", r)
        if pe is not None:
            rules_end[pe[0]] = pe[1]
        elif po is not None:
            rules_or[po[0]] = [po[1].split(" "), po[2].split(" ")]
        elif p is not None:
            rules[p[0]] = p[1].split(" ")

    for m in input[sp + 1 :]:
        messages.append(m)

    return rules, rules_end, rules_or, messages


def get_msg_count(input: list) -> int:
    rules, rules_end, rules_or, messages = get_rules_messages(input)
    correct = get_correct_msg_count(rules, rules_end, rules_or, messages)
    return correct


def get_correct_msg_count(rules, rules_end, rules_or, messages):
    pos = []
    rule_0 = rules["0"]
    for r in rule_0:
        new_pos = get_possibilities(r, rules, rules_end, rules_or)
        pos = and_concat(pos, new_pos)
    spos = set(pos)
    smes = set(messages)
    return len(smes.intersection(spos))


def get_possibilities(r, rules, rules_end, rules_or):
    if r in rules_end:
        return [rules_end[r]]
    elif r in rules:
        return process_rule(rules[r], rules, rules_end, rules_or)
    elif r in rules_or:
        or1 = process_rule(rules_or[r][0], rules, rules_end, rules_or)
        or2 = process_rule(rules_or[r][1], rules, rules_end, rules_or)
        return or1 + or2


def process_rule(rtuple, rules, rules_end, rules_or):
    li = []
    for e in rtuple:
        exp = get_possibilities(e, rules, rules_end, rules_or)
        li = and_concat(li, exp)
    return li


def and_concat(l1, l2):
    if l1 == []:
        return l2
    return [a + b for a in l1 for b in l2]


def get_msg_count_2(input: list) -> int:
    rules, rules_end, rules_or, messages = get_rules_messages(input)
    rules_or["11"] = [["42", "31"], ["42", "11", "31"]]
    rules_or["8"] = [["42"], ["42", "8"]]
    pos_42 = get_possibilities("42", rules, rules_end, rules_or)
    pos_31 = get_possibilities("31", rules, rules_end, rules_or)
    pos = []
    rule_0 = rules["0"]
    for r in rule_0:
        new_pos = get_possibilities(r, rules, rules_end, rules_or)
        pos = and_concat(pos, new_pos)
    spos = set(pos)
    smes = set(messages)

    count = len(smes.intersection(spos))

    non_matching = smes - spos
    n = len(pos_42[0])
    for m in non_matching:
        if len(m) % n == 0:
            chunks = get_string_chunks(m, n)
            s = [
                int(chunk in pos_42)
                for chunk in chunks
                if chunk in pos_42 or chunk in pos_31
            ]
            if (
                len(s) == len(chunks)
                and s[0] == 1
                and s[1] == 1
                and s[len(s) - 1] == 0
                and len(s) - 1 - s[::-1].index(1) < s.index(0)
                and sum(s) > len(s) // 2
            ):
                count += 1

    return count


def get_string_chunks(m, n):
    chunks = [m[i : i + n] for i in range(0, len(m), n)]
    return chunks
