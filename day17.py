
import sys
from collections import defaultdict
import itertools

grid = defaultdict(int)
for row, line in enumerate(sys.stdin.readlines()):
    line.strip()
    for col, thing in enumerate(line):
        grid[(row, col, 0, 0)] = 1 if thing == "#" else 0

def count_neighbours(grid, x, y, z, w):
    return sum(grid[(x + dx, y + dy, z + dz, w + dw)] for dx, dy, dz, dw in itertools.product((-1, 0, 1), repeat=4) if (dx, dy, dz, dw) != (0, 0, 0, 0))

for _ in range(6):
    new_grid = defaultdict(int)
    active_count = 0
    for row in range(-7, 15):
        for col in range(-7, 15):
            for z in range(-7, 7):
                for w in range(-7, 7):
                    num_neighbours = count_neighbours(grid, row, col, z, w)
                    coords = (row, col, z, w)
                    old_value = grid[coords]
                    new_grid[coords] = old_value
                    if old_value == 0 and num_neighbours == 3:
                        new_grid[coords] = 1
                    elif old_value == 1 and num_neighbours not in (2, 3):
                        new_grid[coords] = 0
                    active_count += new_grid[coords]
    grid = new_grid
    print(active_count)
