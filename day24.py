
import sys
from collections import defaultdict

lookup = {
    "nw": (-1, 0), "ne": (-1, 1),
    "w": (0, -1), "e": (0, 1),
    "sw": (1, -1), "se": (1, 0),
}

tiles = defaultdict(int)
# 0 = white, 1 = black
for line in sys.stdin.readlines():
    line = line.strip()
    x, y = 0, 0
    idx = 0
    while idx < len(line):
        dir = line[idx]
        if dir in "ns":
            next = line[idx + 1]
            dir += next
            idx += 1
        idx += 1
        dx, dy = lookup[dir]
        x, y = x + dx, y + dy
    tiles[(x, y)] = 1 - tiles[(x, y)]

print(sum(tiles.values()))

for _ in range(100):
    counts = defaultdict(int)
    for (x, y), on in tiles.items():
        for dx, dy in lookup.values():
            counts[(x + dx, y + dy)] += on
    for pos, count in counts.items():
        assert 0 <= count <= 6
        if tiles[pos] == 1 and count not in (1, 2):
            tiles[pos] = 0
        elif tiles[pos] == 0 and count == 2:
            tiles[pos] = 1
    for pos, value in tiles.items():
        if pos not in counts:
            tiles[pos] = 1 - value


print(sum(tiles.values()))
