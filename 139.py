from math import sqrt, gcd
import time

st = time.time()
lim = 10 ** 8


def solve():
    ans = 0
    for m in range(2, int(sqrt(lim))):
        for n in range(1, m):
            if (m + n) % 2 == 0:
                continue
            if gcd(m, n) != 1:
                continue
            a = m * m - n * n
            b = 2 * m * n
            c = m * m + n * n
            if a+b+c>lim:
                break
            if c % abs(b - a) == 0:
                ans += lim // (a + b + c)
    return ans

print('ans =', solve())
print(time.time() - st, 's')
