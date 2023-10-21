import time

st = time.time()
from math import sqrt


def S(n):
    lim = int(sqrt(n))
    count = [0] + [1] * lim
    for i in range(lim, 0, -1):
        count[i] = n // i // i - sum(count[i * j] for j in range(2, lim // i + 1))
        count[i]%=MOD
    return sum((i*i*count[i])%MOD for i in range(len(count)))%MOD


def solve():
    return S(N)


N = 10 ** 14
MOD = 10 ** 9 + 7
print('ans = ', solve())
# print(is_47_smooth(2491))
print(time.time() - st, 's')
