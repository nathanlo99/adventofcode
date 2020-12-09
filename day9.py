
import sys

last25 = []
idx = 0
target = -1
numbers = []
for line in sys.stdin.readlines():
    num = int(line)
    numbers.append(num)
    if len(last25) != 25:
        last25.append(num)
        continue
    found = False
    for i, ni in enumerate(last25):
        for j, nj in enumerate(last25):
            if j > i and num == ni + nj:
                found = True
                break
        if found:
            break
    if not found:
        target = num
        break
    last25[idx] = num
    idx = (idx + 1) % 25

print("target = ", target)

prefix_sums = [0]
for num in numbers:
    prefix_sums.append(prefix_sums[-1] + num)

# prefix_sums[i] is the sum of everything from 0 to i - 1
for i, pi in enumerate(prefix_sums):
    for j, pj in enumerate(prefix_sums):
        if pj - pi == target and j - i > 1:
            things = numbers[i : j]
            print(min(things) + max(things))
