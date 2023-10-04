import time
from fractions import Fraction as f
import euler
import math

st = time.time()
lim = 10 ** 10


def form(p, n):
    return math.pow(p + 1, n) + math.pow(p - 1, n)


def solve():
    prime = euler.list_primes(10 ** 6)

    for i in range(len(prime)):
        p = prime[i]
        ans = pow(p + 1, i+1, p * p) + pow(p - 1, i+1, p * p)
        ans%=p*p
        if ans>lim:
            return i+1


print('ans =', solve())
print(time.time() - st, 's')
