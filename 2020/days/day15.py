def get_nth_spoken(input: list, stop: int = 2020) -> int:
    nums = [int(n) for n in input[0].split(",")]
    turns = {}
    prev = None
    for i in range(stop):
        if i < len(nums):
            n = nums[i]
        else:
            n = 0 if prev not in turns else i - 1 - turns.get(prev)

        turns[prev] = i - 1
        prev = n
    return n
