import time
import sys
sys.setrecursionlimit(10**6)
st = time.time()
days = 30
LATE_LIMIT = 1
ABSENT_LIMIT = 3


def recur(days, absent, late):
    global mem

    if (days, absent, late) in mem:
        return mem[(days, absent, late)]
    if late > LATE_LIMIT:
        return 0
    if absent == ABSENT_LIMIT:
        return 0

    if days==0:
        return 1
    # student is on time
    ans = recur(days - 1, 0, late)

    # student is late
    ans += recur(days - 1, 0, late + 1)

    # student is absent
    ans += recur(days - 1, absent + 1, late)
    mem[days, absent, late] = ans
    return ans


def solve():
    return recur(30, 0, 0)


mem = {}
ans = 0
print('ans =', solve())
print(time.time() - st, 's')
