
import sys

jolts = [0]
for line in sys.stdin.readlines():
    jolts.append(int(line))

jolts.sort()

target = jolts[-1] + 3
jolts.append(target)

num_ones = 0
num_threes = 0

for cur, next in zip(jolts[:-1], jolts[1:]):
    if next - cur == 1:
        num_ones += 1
    elif next - cur == 3:
        num_threes += 1

print(num_ones, num_threes)
print(num_ones * num_threes)

memo = dict()
def num_ways(start_idx):
    if start_idx in memo:
        return memo[start_idx]

    if start_idx == len(jolts) - 1:
        return 1
    ans = 0
    for i in range(1, 4):
        next_idx = start_idx + i
        if next_idx < len(jolts) and jolts[next_idx] - jolts[start_idx] <= 3:
            ans += num_ways(next_idx)
    memo[start_idx] = ans
    return ans

print(num_ways(0))
