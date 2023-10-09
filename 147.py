import itertools
import math

import euler
import time

st = time.time()


def calc(n, m):
    if n > m:
        n, m = m, n
    normal_sqaure = n * m * (n + 1) * (m + 1) / 4
    # print("normal_sqaure", normal_sqaure)
    dig = []
    dig2 = []

    for c in range(n, -m - 1, -1):
        x1 = max(0, -c)
        x2 = min(n - c, m)
        x3 = x2 - x1
        if x3 > 0:
            dig.append(x3)
            # ans += x3 * x3
        c1 = c + 0.5
        x1 = max(0, -c1)
        x2 = min(n - c1, m)
        x3 = x2 - x1
        if x3 > 0:
            dig2.append(x3)
            # ans += ((x3 * 2) + 1) ** 2
    # print('dig1', dig)
    # print('dig2', dig2)
    ans = 0
    # print(dig, ans)
    for s in range(1, n + 1):
        if s % 2:
            for i in range(len(dig2)):
                x4 = (dig2[i] - s) * 2 + 1
                if x4 > 0:

                    ans += x4 * x4

        else:
            for i in range(len(dig)):
                x4 = (dig[i] - s + 0.5) * 2
                if x4 > 0:
                    ans += x4 * x4

    return int(ans + normal_sqaure)


def form(n, m):
    if m < n: m, n = n, m
    hvr = m * (m + 1) * n * (n + 1) // 4  # Horizontal & vertical
    dr = n * ((2 * m - n) * (4 * n * n - 1) - 3) // 6  # Diagonal
    # print(dr)
    return hvr + dr


def solve():
    ans = 0
    for m in range(1, M+1):
        for n in range(1,N+1):
            ans+=calc(n,m)

    return int(ans)


N, M = 43, 47
print('ans =', solve())
n, m = 1,2
# print(calc(n, m), form(n, m))
# print(pow(10,2,7))
print(time.time() - st, 's')
