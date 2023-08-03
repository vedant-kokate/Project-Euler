import itertools
import math

import euler
import time
from decimal import Decimal, getcontext
st = time.time()
lim = 10 ** 3
goal = 2
def binomial_coefficient(n, k):
    if k > n:
        return 0
    result = 1
    for i in range(1, k + 1):
        result *= n - i + 1
        result //= i
    return result

def probability_of_at_least_k_heads(n, k, p):
    probability = Decimal(0)
    for i in range(k, n + 1):
        probability += Decimal(binomial_coefficient(n, i)) * (p ** i) * ((1 - p) ** (n - i))
    return probability

def binomial_coefficient(n, k):
    if k > n:
        return 0
    result = 1
    for i in range(1, k + 1):
        result *= n - i + 1
        result //= i
    return result
def min_num_of_heads(f):
    ans = 0

    for heads in range(lim + 1):
        if pow(1 - f, lim - heads) * pow(1 + 2 * f, heads) > goal:
            return heads
    return 1000


def solve():
    ans = 1000
    i=0
    a=[]
    val=0
    while i<1:
        x=min_num_of_heads(i)
        if x>ans:
            a.append(x)
        if len(a)>5:
            break
        if x<ans:
            ans=x
            val=i

        i+=0.001
    print(val,'val',ans)
    return round(probability_of_at_least_k_heads(lim, ans, Decimal(0.5)),12)

print('ans =', solve())
print(time.time() - st, 's')



