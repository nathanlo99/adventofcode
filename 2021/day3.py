
import sys
from collections import defaultdict

lines = [s.strip() for s in sys.stdin.readlines()]
nums = map(int, lines)

ans = 0
length = len(lines[0])
count = defaultdict(int)
num = len(lines)
for line in lines:
    for i, c in enumerate(line.strip()):
        count[i] += int(c)

gamma = ""
eps = ""
for i in range(length):
    if count[i] > num / 2:
        gamma += "1"
        eps += "0"
    else:
        gamma += "0"
        eps += "1"

gamma = int(gamma, 2)
eps = int(eps, 2)

print(gamma * eps)


def get_most_common(nums, idx):
    count = 0
    for thing in nums:
        count += int(thing[idx])
    return "1" if count >= len(nums) / 2 else "0"


def get_least_common(nums, idx):
    return "1" if get_most_common(nums, idx) == "0" else "0"


def filter_nums(nums, idx, value):
    return [thing for thing in nums if thing[idx] == value]


def get_oxy(nums):
    idx = 0
    while len(nums) > 1:
        value = get_most_common(nums, idx)
        nums = filter_nums(nums, idx, value)
        idx += 1
    return nums[0]


def get_co2(nums):
    idx = 0
    while len(nums) > 1:
        value = get_least_common(nums, idx)
        nums = filter_nums(nums, idx, value)
        idx += 1
    return nums[0]


oxy = int(get_oxy(lines), 2)
co2 = int(get_co2(lines), 2)
print(oxy * co2)
