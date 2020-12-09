import re

gold = "shiny gold"
bagreg = r"\d*\s*(\w+\s*\w+)\s*bag."
bagreg_numbers = r"(\d*)\s*(\w+\s*\w+)\s*bag."
nobag = "no other"


def get_count(input: list) -> int:
    rules = []
    bags_with = set()
    for rule in input:
        bags = re.findall(bagreg, rule)
        if any(nobag in s for s in bags) is False:
            rules.append(bags)
    new_rules = rules
    bags = set()
    while new_rules != []:
        new_rules, bags = parse_rules(new_rules, bags_with)
        if bags == bags_with:
            bags_with.update(bags)
            break
        bags_with.update(bags)

    return len(bags_with)


def parse_rules(rules, bags_with):
    new_rules = []
    bags_w = bags_with.copy()
    for rule in rules:
        if any(gold in s for s in rule[1:]):
            bags_w.add(rule[0])
        else:
            new_rules.append(rule)
    for rule in new_rules:
        for bag in bags_w:
            for i in range(1, len(rule)):
                if rule[i] == bag:
                    rule[i] = gold
    return new_rules, bags_w


def get_count_2_2(input: list) -> int:
    final_count = 0
    rules = []
    bags_gold = {}
    bags_empty = {}
    for rule in input:
        bags = re.findall(bagreg_numbers, rule)
        if gold in bags[0]:
            for rest in bags[1:]:
                bags_gold[rest[1]] = int(rest[0])
        if any(nobag in s for s in bags) is False:
            rules.append(bags)
        else:
            bags_empty[bags[0][1]] = 0
    final_count = sum(
        [
            count * get_empty_bags(bag, rules, bags_empty)
            for bag, count in bags_gold.items()
        ]
    )
    return final_count


def get_empty_bags(bag, rules, bags_empty):
    count = 1
    for bags in rules:
        if bag in bags[0]:
            for rest in bags[1:]:
                inner_count = int(rest[0])
                if rest[1] in bags_empty:
                    count += inner_count
                else:
                    count += inner_count * get_empty_bags(rest[1], rules, bags_empty)
    return count
