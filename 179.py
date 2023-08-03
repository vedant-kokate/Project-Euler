import euler
import time

st = time.time()
lim = 10 ** 7 + 1


def solve():
    a = [0] * lim
    for i in range(2, (lim+1) // 2):
        for j in range(i * 2, lim, i):
            a[j] += 1
    ans = 0
    for i in range(2, lim - 1):
        if a[i] == a[i + 1]:
            ans += 1
    return ans


print('ans =', solve())
print(time.time() - st, 's')
