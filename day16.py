
import sys
from collections import defaultdict

restrictions = dict()
while True:
    line = input().strip()
    if line == "":
        break
    description, ranges = line.split(":")
    range1, range2 = ranges.split(" or ")
    s1, e1 = map(int, range1.split("-"))
    s2, e2 = map(int, range2.split("-"))
    restrictions[description] = ((s1, e1), (s2, e2))

assert(input().strip() == "your ticket:")
my_ticket = list(map(int, input().split(",")))

tickets = []
input(), input()
while True:
    try:
        line = input().strip()
    except:
        break
    tickets.append(list(map(int, line.split(","))))

ticket_length = len(tickets[0])
ans = 0
valid_tickets = []
for ticket in tickets:
    valid = True
    for number in ticket:
        for (s1, e1), (s2, e2) in restrictions.values():
            if s1 <= number <= e1 or s2 <= number <= e2:
                break
        else:
            ans += number
            valid = False
    if valid:
        # Valid ticket
        valid_tickets.append(ticket)

possibilities = defaultdict(list)
for idx in range(ticket_length):
    for description, ranges in restrictions.items():
        (s1, e1), (s2, e2) = ranges
        for ticket in valid_tickets:
            number = ticket[idx]
            if not (s1 <= number <= e1 or s2 <= number <= e2):
                break
        else:
            possibilities[description].append(idx)

queue = []
answers = dict()
for description in possibilities:
    if len(possibilities[description]) == 1:
        queue.append(description)

while queue:
    desc = queue[-1]
    cand = possibilities[desc][0]
    queue = queue[:-1]
    answers[desc] = cand
    for description in possibilities:
        if cand in possibilities[description]:
            possibilities[description].remove(cand)
            if len(possibilities[description]) == 1:
                queue.append(description)

part2_ans = 1
for description in restrictions:
    if description.startswith("departure"):
        part2_ans *= my_ticket[answers[description]]

print(ans)
print(part2_ans)
