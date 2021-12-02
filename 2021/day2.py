
import sys

lines = sys.stdin.readlines()
nums = map(int, lines)

x, y = 0, 0
for line in lines:
    dir, amt = line.split()
    amt = int(amt)
    if dir == "forward":
        x += amt
    elif dir == "down":
        y += amt
    elif dir == "up":
        y -= amt

print(x * y)

x, y, aim = 0, 0, 0
for line in lines:
    dir, amt = line.split()
    amt = int(amt)
    if dir == "forward":
        x += amt
        y += aim * amt
    elif dir == "down":
        aim += amt
    elif dir == "up":
        aim -= amt
print(x * y)
