
import sys

grid = []
for line in sys.stdin.readlines():
    grid.append(list(line.strip()))

def print_grid(grid):
    for row in grid:
        print("".join(row))

def get_num_adj(grid, row, col):
    ans = 0
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            if (dx, dy) != (0, 0):
                cur_row, cur_col = row + dy, col + dx
                while 0 <= cur_row < len(grid) and 0 <= cur_col < len(grid[0]) and grid[cur_row][cur_col] == ".":
                    cur_col += dx
                    cur_row += dy

                if 0 <= cur_row < len(grid) and 0 <= cur_col < len(grid[0]) and grid[cur_row][cur_col] == "#":
                    ans += 1
                # Part 1
                # next_row, next_col = row + dx, col + dy
                # if 0 <= next_row < len(grid) and 0 <= next_col < len(grid[0]) and grid[next_row][next_col] == "#":
                #     ans += 1
    return ans

width, height = len(grid[0]), len(grid)

while True:
    num_changed = 0
    num_occupied = 0
    new_grid = [[y for y in x] for x in grid]
    for row in range(0, height):
        for col in range(0, width):
            num_adj = get_num_adj(grid, row, col)
            if grid[row][col] == "L" and num_adj == 0:
                new_grid[row][col] = "#"
                num_changed += 1
            elif grid[row][col] == "#" and num_adj >= 5:
                new_grid[row][col] = "L"
                num_changed += 1
            num_occupied += 1 if new_grid[row][col] == "#" else 0
    if num_changed == 0:
        print(num_occupied)
        break
    grid = new_grid
