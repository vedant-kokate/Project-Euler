import time

st = time.time()
lim = 10**9


def solve():
    n = lim // 3
    ans = n*(n + 1) // 2 - 1
    return ans * 6


print('ans =', solve())
print(time.time() - st, 's')
