
import sys

ans = 0
alpha = "abcdefghijklmnopqrstuvwxyz"
seen = set()
intersection = set(alpha)
for line in sys.stdin.readlines():
    if line.strip() == "":
        ans += len(seen & intersection)
        seen = set()
        intersection = set(alpha)
        continue
    new = set(line.strip())
    seen |= new
    intersection &= new
ans += len(seen & intersection)

print(ans)
