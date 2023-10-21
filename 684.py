import time
import euler
from math import sqrt

st = time.time()


def S(k):
    q = k // 9
    r = k % 9
    return (6 * (pow(10, q, MOD) - 1) - (9 * q % MOD) + r * 500000004 * (
                r * pow(10, q, MOD) + 3 * pow(10, q, MOD) - 2)) % MOD


def solve():
    f = [0, 1]
    while len(f) < 91:
        f.append(f[-1] + f[-2])
    return sum(S(k) % MOD for k in f[2:]) % MOD


MOD = 1000000007
print('ans = ', solve())
# print(is_47_smooth(2491))
print(time.time() - st, 's')
