import itertools
import math

import euler
import time

st = time.time()
lim = 10 ** 6+3

def form(x):
    return math.floor(pow(2,30.403243784-x*x))/(10**9)
def solve():
    ans = 0
    u=-1
    a=[]
    for i in range(1000):
        u=form(u)
        a.append(u)
        if len(a)>2:
            a.pop(0)
    return sum(a)


print('ans =', solve())
# print(pow(10,2,7))
print(time.time() - st, 's')
