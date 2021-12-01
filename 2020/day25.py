
num1, num2 = int(input()), int(input())
p = 20201227

def order(num, base, p):
    cur = 1
    ans = 0
    while cur != num:
        cur = (cur * base) % p
        ans += 1
    return ans

def exp(expt, base, p):
    print("exp", expt, base, p)
    if expt == 0:
        return 1
    root = exp(expt // 2, base, p)
    ans = (root * root) % p
    if expt % 2 == 1:
        ans = (ans * base) % p
    return ans

a = order(num1, 7, p)
b = order(num2, 7, p)
product = (a * b) % (p - 1)
print(product)
print(exp(product, 7, p))
