import itertools
import math
from heapq import heapify, heappop, heappush
import time

st = time.time()




def solve():
    inv = pow(1504170715041707, -1, 4503599627370517)
    ans = [NUM]
    ans2 = []
    max_ = MOD
    for i in itertools.count(1):
        x = NUM * i % MOD
        if x < ans[-1]:
            ans.append(x)
        if x < 2 * 10 ** 7:
            break
        y = inv * i % MOD
        if y < max_:
            max_ = y
            ans2.append(i)
    return sum(set(ans+ans2))


NUM = 1504170715041707
MOD = 4503599627370517
print('ans = ', solve())
print(time.time() - st, 's')
