
import sys

trees = list(sys.stdin.readlines())
def count_trees(dx, dy):
    idx = 0
    idy = 0
    num_trees = 0
    for line in trees:
        line = line.strip()
        line_length = len(line)
        if idy % dy == 0 and line[idx] == '#':
            num_trees += 1
        if idy % dy == 0:
            idx = (idx + dx) % line_length
        idy = idy + 1
    return num_trees

ans = 1
ans *= count_trees(1, 1)
ans *= count_trees(3, 1)
ans *= count_trees(5, 1)
ans *= count_trees(7, 1)
ans *= count_trees(1, 2)
print(ans)
