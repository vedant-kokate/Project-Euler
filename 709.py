import itertools
import math
from heapq import heapify, heappop, heappush
import time

st = time.time()


def A001250_list(n):
    A000111_list, blist = [1, 1], [1]
    for i in range(n - 1):
        blist = [(x % MOD) for x in list(reversed(list(accumulate(reversed(blist))))) + [0]] if i % 2 else [0] + [(x % MOD) for x in list(accumulate(blist))]
        A000111_list.append(sum(blist) % MOD)
    # print(blist)
    return A000111_list[-1]
def solve():
    return A001250_list(N)


N = 24680
MOD = 1020202009
print('ans = ', solve())
print(time.time() - st, 's')
