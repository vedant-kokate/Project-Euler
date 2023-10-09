import time
from functools import cache

st = time.time()
LIM = 20


@cache
def dp(x, y, pos, target):
    xy = x + y
    if pos == target - 1:
        return 9 - xy + 1

    res = 0
    for i in range(10):
        if xy + i <= 9:
            res += dp(y, i, pos + 1, target)

    return res


def solve():
    ans = 0
    for x in range(1, 10):
        for y in range(10):
            if x + y <= 9:
                ans += dp(x, y, 2, LIM)
    return ans


print('ans =', solve())

print(time.time() - st, 's')
