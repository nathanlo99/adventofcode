
import sys

nums = list(map(int, sys.stdin.readlines()))
ans = 0
for prev, next in zip(nums[:-1], nums[1:]):
    if next > prev:
        ans += 1
print(ans)

second_ans = 0
prev = 10000000
for a, b, c in zip(nums[:-2], nums[1:-1], nums[2:]):
    this_sum = a + b + c
    if this_sum > prev:
        second_ans += 1
    prev = this_sum
print(second_ans)
