
import sys
from collections import defaultdict

last_seen = dict()

starting = list(map(int, input().split(",")))
for i, num in enumerate(starting):
    last_seen[num] = i + 1
last = starting[-1]
idx = len(starting)

for i in range(idx, 30000000):
    if last in last_seen:
        next = i - last_seen[last]
    else:
        next = 0
    last_seen[last] = i
    last = next

print(last)
