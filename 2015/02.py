from aocd import get_data

# surface area 2*l*w + 2*w*h + 2*h*l + area of smallest side..


def paper(data):
    boxes = [list(map(int, box.strip().split("x"))) for box in data.split("\n")]
    paper = 0
    for box in boxes:
        prods = [a * b for a, b in zip(box, box[1:] + box[:1])]
        paper += 2 * sum(prods) + min(prods)
    print(paper)
    return paper


def ribbon(data):
    boxes = [list(map(int, box.strip().split("x"))) for box in data.split("\n")]
    ribbon = 0
    for b in boxes:
        b.sort()
        ribbon += 2 * b[0] + 2 * b[1] + b[0] * b[1] * b[2]
    print(ribbon)
    return ribbon


def test_floors():
    d = "2x3x4\n1x1x10"
    assert paper(d) == 101


def test_ribbon():
    d = "2x3x4\n1x1x10"
    assert ribbon(d) == 48


data = get_data(day=2, year=2015)
paper(data)
ribbon(data)
