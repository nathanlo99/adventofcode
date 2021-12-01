
import sys

num_valid = 0
num_valid2 = 0
for line in sys.stdin.readlines():
    requirement, password = line.split(':')
    # Note the password has an extra space in front, which accounts for
    # 1-indexing later
    occurrence_range, letter = requirement.split(' ')
    a, b = map(int, occurrence_range.split('-'))
    # Part 1: The old policy
    if a <= password.count(letter) <= b:
        num_valid += 1
    num_occurrences = int(password[a] == letter) + int(password[b] == letter)
    if num_occurrences == 1:
        num_valid2 += 1

print(num_valid)
print(num_valid2)
