from math import gcd, sqrt, ceil, floor

import time
from fractions import Fraction as f

st = time.time()
lim = 100


def solve2():
    def form(a, b, c, d):
        if a == c == b == d:
            return 1
        if a == c and b == d:
            return 2
        if a == c or b == d:
            return 4
        if a == b and c == d:
            return 4
        return 8

    def solver(a, b, c, d):
        # if (a, b, c, d) in memo:
        #     return memo[(a, b, c, d)]
        area = (a + c) * (b + d)
        boundary = g[(a, b)] + g[(b, c)] + g[(c, d)] + g[(a, d)]
        internal = (area - boundary) / 2 + 1
        i_sq = sqrt(internal)
        i_bool = ceil(i_sq) == floor(i_sq)
        # temp = set()
        if i_bool:
            f = form(a, b, c, d)
            # memo[(a, b, c, d)] = f
            # print(a, b, c, d,f)
            return f

        return 0

    ans = 0
    g = {}
    # memo = {}
    for i in range(1, lim + 1):
        for j in range(i, lim + 1):
            x = gcd(i, j)
            g[(i, j)] = x
            g[(j, i)] = x

    for a in range(1, lim + 1):
        for b in range(a, lim + 1):
            for c in range(b, lim + 1):
                for d in range(c, lim + 1):
                    # ans += solver(a, b, c, d) + solver(a, b, d, c) + solver(a, c, b, d)
                    ans += solver(a, b, c, d)
                    if a != b and (a, b, c, d) != (a, b, d, c):
                        ans += solver(a, b, d, c)
                    if a != d and (a, b, c, d) != (a, c, b, d):
                        ans += solver(a, c, b, d)
    return ans


def solve():
    def solver(a, b, c, d):
        area = (a + c) * (b + d)
        boundary = g[(a, b)] + g[(b, c)] + g[(c, d)] + g[(a, d)]
        internal = (area - boundary) / 2 + 1
        i_sq = sqrt(internal)
        i_bool = ceil(i_sq) == floor(i_sq)
        # temp = set()
        if i_bool:
            # print(a,b,c,d)
            return 1

        return 0

    ans = 0
    g = {}
    for i in range(1, lim + 1):
        for j in range(i, lim + 1):
            x = gcd(i, j)
            g[(i, j)] = x
            g[(j, i)] = x

    for a in range(1, lim + 1):
        for b in range(1, lim + 1):
            for c in range(1, lim + 1):
                for d in range(1, lim + 1):
                    # ans += solver(a, b, c, d) + solver(a, b, d, c) + solver(a, c, b, d)
                    ans += solver(a, b, c, d)
                    # if a != b:
                    #     ans += solver(a, b, d, c)
                    # if (a, b, c, d) != (a, c, b, d):
                    #     ans += solver(a, c, b, d)
    return ans


# print('ans = ', solve())
# print(time.time() - st, 's')
# st = time.time()
print('ans = ', solve2())
print(time.time() - st, 's')
