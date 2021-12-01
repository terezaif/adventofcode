def get_handshake(input: list) -> int:
    cp = int(input[0])
    dp = int(input[1])

    subj = 7
    cloops = rev_handshake(cp, subj)
    enc = handshake(dp, cloops)
    return enc


def rev_handshake(p, subj):
    v = 1
    div = 20201227
    i = 0
    while v != p:
        v *= subj
        v = v % div
        i += 1
    return i


def handshake(subj, loops):
    v = 1
    div = 20201227
    while loops > 0:
        v *= subj
        v = v % div
        loops -= 1
    return v
