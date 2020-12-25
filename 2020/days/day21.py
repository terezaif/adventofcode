from parse import parse


def parse_input(input):
    food = []
    for line in input:
        p = parse("{} (contains {})", line)
        if p:
            ingreds = set(p[0].split(" "))
            allerg = set(p[1].split(", "))
        # print(p, ingreds, alerg)
        food.append([ingreds, allerg])

    return food


def get_goodfood_count(input: list) -> int:
    food = parse_input(input)
    allergens = {}
    for f in food:
        for a in f[1]:
            ins = (
                set(f[0])
                if a not in allergens
                else set(f[0]).intersection(allergens.get(a))
            )
            allergens[a] = ins
    bad = set()
    for a, f in allergens.items():
        bad |= f

    good = [ff for f in food for ff in f[0] if ff not in bad]
    return len(good)


def get_badfood(input: list) -> int:
    food = parse_input(input)
    allergens = {}
    for f in food:
        for a in f[1]:
            ins = (
                set(f[0])
                if a not in allergens
                else set(f[0]).intersection(allergens.get(a))
            )
            allergens[a] = ins

    cleana = {}
    for a, f in allergens.items():
        if len(f) == 1:
            cleana[f.pop()] = a
        else:
            allergens[a] = list(f)
    for f, a in cleana.items():
        allergens.pop(a)

    while len(allergens) > 0:
        for a, f in allergens.items():
            for ff in f:
                if ff in cleana:
                    f.remove(ff)
            if len(f) == 1:
                cleana[f[0]] = a
            else:
                allergens[a] = f
        for f, a in cleana.items():
            allergens.pop(a, None)
    bad = [k for k, v in sorted(cleana.items(), key=lambda item: item[1])]
    badlist = ",".join(bad)
    return badlist
