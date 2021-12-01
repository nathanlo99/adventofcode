
import sys
import copy
from collections import defaultdict

possibilities = dict()
count = defaultdict(int)
for line in sys.stdin.readlines():
    line = line.strip()[:-1]
    ingredients, allergens = line.split("(")
    assert(allergens.startswith("contains "))
    allergens = allergens[len("contains "):].split(", ")
    ingredients = set(ingredients.split())
    for allergen in allergens:
        if allergen in possibilities:
            possibilities[allergen] &= ingredients
        else:
            possibilities[allergen] = set(ingredients)
    for ingredient in ingredients:
        count[ingredient] += 1

queue = []
for allergen, things in possibilities.items():
    if len(things) == 1:
        queue.append(allergen)

answers = dict()
while queue:
    allergen = queue[0]
    queue = queue[1:]
    choice = possibilities[allergen].pop()
    answers[allergen] = choice
    for other_allergen, things in possibilities.items():
        if choice in things:
            possibilities[other_allergen].remove(choice)
            if len(possibilities[other_allergen]) == 1:
                queue.append(other_allergen)

ans1 = sum(count[thing] for thing in count.keys() if thing not in answers.values())
ans2 = ",".join(answers[allergen] for allergen in sorted(answers.keys()))

print(ans1)
print(ans2)
