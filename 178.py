import time
from functools import cache

st = time.time()

LIM = 40
Total_dig = 10
ALL_FOUND = (1 << Total_dig) - 1


@cache
def dp(dig, pos, lim, dig_found, ):
    dig_found |= 1 << dig
    if pos == lim:
        if dig_found == ALL_FOUND:
            return 1
        else:
            return 0

    pos += 1

    res = 0
    if dig > 0:
        res += dp(dig - 1, pos, lim, dig_found)

    if dig < 9:
        res += dp(dig + 1, pos, lim, dig_found)

    return res


def solve():
    ans = 0
    for lim in range(1, LIM ):
        for dig in range(1, Total_dig):
            ans += dp(dig, 0, lim, 0)

    return ans


print('ans =', solve())
# print(dp(0, dig, digs))
print(time.time() - st, 's')
