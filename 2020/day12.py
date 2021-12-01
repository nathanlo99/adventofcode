
import sys
from math import sin, cos, radians

x, y, angle = 0, 0, 0
wx, wy = 10, 1
for line in sys.stdin.readlines():
    op = line[0]
    num = int(line[1:])
    if op == "F":
        x += wx * num
        y += wy * num
    elif op == "N":
        wy += num
    elif op == "S":
        wy -= num
    elif op == "E":
        wx += num
    elif op == "W":
        wx -= num
    elif op == "L":
        a, b = wx, wy
        c, d = cos(radians(num)), sin(radians(num))
        wx, wy = a * c - b * d, a * d + b * c
    elif op == "R":
        a, b = wx, wy
        c, d = cos(radians(-num)), sin(radians(-num))
        wx, wy = a * c - b * d, a * d + b * c

print(abs(x) + abs(y))
