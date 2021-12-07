
from collections import defaultdict

nums = list(sorted(map(int, input().split(","))))

a, b = min(nums), max(nums)


def get_cost(x, y):
    diff = abs(y - x)
    return diff * (diff + 1) / 2.


min_cost = 100000000000000
for i in range(a, b + 1):
    cost = sum(get_cost(x, i) for x in nums)
    min_cost = min(min_cost, cost)
print(min_cost)
