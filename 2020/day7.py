
import sys
from collections import defaultdict, deque

next = defaultdict(set)
contains = defaultdict(dict)
for line in sys.stdin.readlines():
    containing, contained = line.strip().split("contain")
    containing_adj1, containing_adj2, _ = containing.split()
    contained = contained.lstrip()[:-1]
    if contained == "no other bags":
        continue
    contained = [x.strip() for x in contained.split(",")]
    for bag in contained:
        num, adj1, adj2, _ = bag.split()
        next[adj1 + "|" + adj2].add(containing_adj1 + "|" + containing_adj2)
        contains[containing_adj1 + "|" + containing_adj2][adj1 + "|" + adj2] = int(num)
    print(contained)

start = "shiny|gold"
seen = set()
queue = deque([start])
while queue:
    cur = queue.pop()
    seen.add(cur)
    for neighbour in next[cur]:
        if neighbour not in seen:
            queue.append(neighbour)

memo = dict()
def get(name):
    if name not in memo:
        ans = 1
        for thing, amt in contains[name].items():
            ans += amt * get(thing)
        memo[name] = ans
    return memo[name]

print(len(seen) - 1)
print(get(start) - 1)

print(memo)
print(contains[start])
