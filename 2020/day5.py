
import sys

ans = 0
seats = set()
for line in sys.stdin.readlines():
    rl, rh = (0, 128)
    cl, ch = (0, 8)

    for c in line:
        rm = (rl + rh) // 2
        cm = (cl + ch) // 2
        if c == "B":
            rl, rh = rm, rh
        elif c == "F":
            rl, rh = rl, rm
        elif c == "R":
            cl, ch = cm, ch
        elif c == "L":
            cl, ch = cl, cm
    id = 8 * rl + cl
    seats.add(id)
    ans = max(ans, id)

for seat in seats:
    if seat + 2 in seats and seat + 1 not in seats:
        print(seat)
print(ans)
