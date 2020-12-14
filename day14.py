
import sys
from collections import defaultdict
def apply_mask(mask, value):
    result = value
    for i, chr in enumerate(mask):
        pow = 2 ** (35 - i)
        if chr == "1":
            result |= pow
        elif chr == "0":
            result &= ~pow
    return result

def get_addrs(mask, addr):
    if mask == "":
        return [ 0 ]
    intermediate = get_addrs(mask[:-1], addr // 2)
    last_mask, last_addr = mask[-1], addr % 2
    if last_mask == "0":
        return [2 * x + last_addr for x in intermediate]
    elif last_mask == "1":
        return [2 * x + 1 for x in intermediate]
    else:
        return [2 * x + 0 for x in intermediate] + [2 * x + 1 for x in intermediate]

mask = ""
memory = defaultdict(int)
second_memory = defaultdict(int)
for line in sys.stdin.readlines():
    line = line.strip()
    if line.startswith("mask = "):
        mask = line[len("mask = "):]
    else:
        open = line.index("[")
        close = line.index("]")
        equals = line.index("=")
        addr = int(line[open + 1:close])
        value = int(line[equals + 1:])
        # Part 1
        memory[addr] = apply_mask(mask, value)

        for floating_addr in get_addrs(mask, addr):
            second_memory[floating_addr] = value

print(sum(memory.values()))
print(sum(second_memory.values()))
