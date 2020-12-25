import math


def get_bus(input: list) -> int:
    ts = int(input[0])
    buses = [int(bus) for bus in input[1].split(",") if bus != "x"]
    closest_bus = 1
    min_diff = ts

    for bus in buses:
        after = (int(ts / bus) + 1) * bus
        if abs(ts - after) < min_diff:
            min_diff = abs(ts - after)
            closest_bus = bus

    return min_diff * closest_bus


def get_bus_2(input: list) -> int:
    def get_s_euclidian_ext(a, b):
        b0 = b
        x0, x1 = 0, 1
        if b == 1:
            return 1
        while a > 1:
            q = a // b
            a, b = b, a % b
            x0, x1 = x1 - q * x0, x0
        if x1 < 0:
            x1 += b0
        return x1

    buses = [
        (int(bus), idx) for idx, bus in enumerate(input[1].split(",")) if bus != "x"
    ]
    N = math.prod([i[0] for i in buses])

    x = 0
    for n, a in buses:  # 344498777506
        p = N // n
        x += (n - a) * get_s_euclidian_ext(p, n) * p

    return x % N
