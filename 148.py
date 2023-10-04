import itertools
import math

import euler
import time

st = time.time()
lim = 10**9


def to_base_7(decimal_number):
    base_7_number = ""

    while decimal_number > 0:
        remainder = decimal_number % 7
        base_7_number = str(remainder) + base_7_number
        decimal_number //= 7

    return [int(x) for x in base_7_number]


def solve():
    num = to_base_7(lim)
    l = len(num)
    ans = []
    for i in range(l):
        f = 1
        for j in range(i):
            f*=num[j]+1
        n = num[i]
        ans.append(n*(n+1)//2*f*28**(l-1-i))
    return sum(ans)
    # for i in range


print('ans =', solve())
# print(pow(10,2,7))
print(time.time() - st, 's')
