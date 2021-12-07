
import sys
from collections import defaultdict

counts = defaultdict(int)
nums = map(int, input().split(","))
for num in nums:
    counts[num] += 1

for i in range(256):
    new_counts = defaultdict(int)
    for num in (1, 2, 3, 4, 5, 6, 7, 8):
        new_counts[num - 1] += counts[num]
    new_counts[8] += counts[0]
    new_counts[6] += counts[0]
    counts = new_counts
print(sum(counts.values()))
