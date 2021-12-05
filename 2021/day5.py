
import sys
from collections import defaultdict

lines = sys.stdin.readlines()

covered = defaultdict(int)

for line in lines:
    begin, end = line.split(" -> ")
    x1, y1 = map(int, begin.split(","))
    x2, y2 = map(int, end.split(","))

    if x1 == x2:
        if y1 > y2:
            y1, y2 = y2, y1
        for i in range(y1, y2 + 1):
            covered[(x1, i)] += 1
    elif y1 == y2:
        if x1 > x2:
            x1, x2 = x2, x1
        for i in range(x1, x2 + 1):
            covered[(i, y1)] += 1
    else:
        dx = 1 if x2 > x1 else -1
        dy = 1 if y2 > y1 else -1
        while x1 != x2:
            covered[(x1, y1)] += 1
            x1 += dx
            y1 += dy
        covered[(x2, y2)] += 1

ans = 0
for point, count in covered.items():
    if count >= 2:
        ans += 1
print(ans)
