import itertools
import time
from math import log10

st = time.time()


def p(L, n):
    l1, l2 = L, L + 1
    l1 /= pow(10, len(str(L))-1)
    l2 /= pow(10, len(str(L))-1)
    # print(l1,l2)
    left = log10(l1)
    right=log10(l2)
    count = 0
    for j in itertools.count(0):
        middle = j*log10(2)-int(j*log10(2))
        if left<middle<right:
            count+=1
        if count==n:
            return j


def solve():
    return p(123,678910)


MOD = 1000000007
print('ans = ', solve())
# print(is_47_smooth(2491))
print(time.time() - st, 's')
