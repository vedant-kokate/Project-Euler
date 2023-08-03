import time
from math import sqrt

st = time.time()
lim = 12000
lim += 1


def factorize(n, sum_, terms, prod):
    if n == 1:
        pos = prod - sum_ + terms
        if pos>=len(a):
            return
        a[pos] = min(a[pos], prod)
    for i in range(2, n + 1):
        if n % i == 0:
            factorize(n // i, sum_ + i, terms + 1, prod * i)


def solve():
    for i in range(2, 2*lim):
        factorize(i, 0, 0, 1)

    ans = sum(set(a[2:]))
    return ans


a = [10 ** 10] * lim

print('ans =', solve())
# print(a)
print(time.time() - st, 's')
