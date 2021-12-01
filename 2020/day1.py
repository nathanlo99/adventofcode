
original_numbers = [int(input()) for _ in range(200)]

# First part
def twosum(numbers, target):
    seen = set()
    for num in numbers:
        if target - num in seen:
            return num, target - num
        seen.add(num)
    return None, None

a, b = twosum(original_numbers, 2020)
print(a * b)

def threesum(numbers, target):
    seen = set()
    for num in numbers:
        a, b = twosum(seen, 2020 - num)
        if a is not None:
            return num, a, b
        seen.add(num)
    return None, None, None

a, b, c = threesum(original_numbers, 2020)
print(a * b * c)



# Second part
