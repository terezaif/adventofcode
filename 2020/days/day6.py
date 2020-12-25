def get_questions_count(input: str) -> int:
    qcount = 0
    qs = set()
    for line in input:
        if line == "":
            qcount += len(qs)
            qs = set()
        else:
            qs.update(list(line))
    qcount += len(qs)

    return qcount


def get_questions_everyone_count(input: str) -> int:
    qcount = 0
    first = True
    qs = set()
    for line in input:
        if line == "":
            qcount += len(qs)
            qs = set()
            first = True
        else:
            if first:
                qs.update(list(line))
                first = False
            else:
                qs = qs.intersection(list(line))
    qcount += len(qs)

    return qcount
