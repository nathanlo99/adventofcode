
cups = list(map(int, input().strip()))
cups += list(range(len(cups), 1000001))

next = dict()
for idx, num in enumerate(cups[:-1]):
    next[num] = cups[idx + 1]
next[cups[-1]] = cups[0]

cur = cups[0]
for _ in range(10000000):
    a = next[cur]
    b = next[a]
    c = next[b]
    next[cur] = next[c]
    held = (a, b, c)
    pick = cur - 1
    while pick in held or pick < 1:
        pick -= 1
        if pick < 1:
            pick = len(next)
    tmp = next[pick]
    next[pick] = a
    next[c] = tmp
    cur = next[cur]

"""
print(next)
result = []
cur = 1
while True:
    result.append(cur)
    cur = next[cur]
    if cur == 1:
        break
print(result)
"""

print(next[1], next[next[1]])
print(next[1] * next[next[1]])
