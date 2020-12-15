def get_memsum(input: list) -> int:
    def update_memory(operations):
        memory = {}
        mask = list(operations[0])
        set_bits = [
            (int(bit), len(mask) - idx - 1)
            for idx, bit in enumerate(list(mask))
            if bit in ["0", "1"]
        ]
        for mem in operations[1:]:
            memory[mem[0]] = resetBits(mem[1], set_bits)
        return memory

    memory = {}
    for operations in input:
        memory.update(update_memory(operations))
    return sum(memory.values())


def setBit(int_type, offset):
    mask = 1 << offset
    return int_type | mask


def clearBit(int_type, offset):
    mask = ~(1 << offset)
    return int_type & mask


def resetBits(number, setbits):
    for bit in setbits:
        if bit[0] == 1:
            number = setBit(int(number), bit[1])
        else:
            number = clearBit(int(number), bit[1])
    return number


def setBits(number, setbits):
    number = int(number)
    for bit in setbits:
        if bit[0] == 1:
            number = number | (1 << bit[1])
    return number


def clearBits(number, setbits):
    for bit in setbits:
        number = clearBit(int(number), bit[1])
    return number


def get_memsum_2(input: list) -> int:
    def get_permutations(X_bits):
        bit_perm = []
        max_bits = (1 << len(X_bits)) - 1
        for i in range(0, max_bits + 1):
            bits = format(i, f"0{len(X_bits)}b")
            bit_perm.append([(int(bits[idx]), x[1]) for idx, x in enumerate(X_bits)])
        return bit_perm

    def update_memory(operations):
        memory = {}
        mask = list(operations[0])

        set_bits = [
            (int(bit), len(mask) - idx - 1)
            for idx, bit in enumerate(list(mask))
            if bit in ["1"]
        ]
        X_bits = [
            (bit, len(mask) - idx - 1)
            for idx, bit in enumerate(list(mask))
            if bit in ["X"]
        ]

        memory_locs_bits = get_permutations(X_bits)

        for mem in operations[1:]:
            number = int(mem[1])
            # number = setBits(mem[1], set_bits)
            # number = clearBits(number, clear_bits)
            mem_loc = setBits(mem[0], set_bits)
            if memory_locs_bits == []:
                memory[mem_loc] = number
            for mem_set_bits in memory_locs_bits:
                new_mem_loc = resetBits(mem_loc, mem_set_bits)
                # print(number, "->", new_mem_loc)
                memory[new_mem_loc] = number
        return memory

    memory = {}
    for operations in input:
        # print(operations)
        memory.update(update_memory(operations))

    return sum(memory.values())
