
import sys

instructions = []
for line in sys.stdin.readlines():
    op, num = line.split()
    instructions.append((op, int(num)))

def run(instructions):
    seen = set()
    idx = 0
    acc = 0
    while idx not in seen and idx < len(instructions):
        seen.add(idx)
        op, num = instructions[idx]
        if op == "nop":
            idx += 1
        elif op == "acc":
            idx += 1
            acc += num
        elif op == "jmp":
            idx += num
    if idx not in seen:
        return True, acc
    else:
        return False, acc

for idx, (op, num) in enumerate(instructions):
    old = (op, num)
    if op == "nop":
        instructions[idx] = ("jmp", num)
    elif op == "jmp":
        instructions[idx] = ("nop", num)
    terminate, acc = run(instructions)
    if terminate:
        print("acc is ", acc)
    instructions[idx] = old
