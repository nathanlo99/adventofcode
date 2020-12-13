
import sys
from math import ceil

start = int(input())
line = input()
ids = [int(x) for x in line.split(",") if x != "x"]

def round_up(n, id):
    return int(ceil(n / id) * id)

def solve(mod1, mod2, a, b):
    print("solve", mod1, mod2, a, b)
    if mod1 < mod2:
        mod1, mod2, a, b = mod2, mod1, b, a
    a %= mod1
    b %= mod2
    for thing in range(mod2):
        candidate = thing * mod1 + a
        if candidate % mod2 == b:
            return candidate % (mod1 * mod2)

wait_times = [round_up(start, id) - start for id in ids]
shortest_wait = min(wait_times)
shortest_id = ids[wait_times.index(shortest_wait)]
print(shortest_wait * shortest_id)

cong = list()
for i, id in enumerate(line.split(',')):
    if id != "x":
        cong.append((int(id) - i, int(id)))
cong.sort(key=lambda x: -x[1])

cur_rem, cur_mod = cong[0]
for rem, mod in cong[1:]:
    print(cur_rem, cur_mod)
    cur_rem, cur_mod = solve(cur_mod, mod, cur_rem, rem), mod * cur_mod
print(cur_rem)
