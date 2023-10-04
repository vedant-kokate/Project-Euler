import time
from random import randint


def form(a):
    mul = [pow(a[i], i + 1) for i in range(len(a))]
    f = 1
    for i in mul:
        f *= i
    return f


def slow(m):
    a = [1] * m

    p = form(a)
    log = [p]
    while True:
        # print(p,a)
        x = randint(0, m - 1)
        y = randint(0, m - 1)
        while y == x:
            y = randint(0, m - 1)

        delta = pow(10, -randint(1, 5))
        old_x, old_y = a[x], a[y]
        a[x] += delta
        a[y] -= delta
        p2 = form(a)

        # print(p2, x, y)
        if p2 < p or a[y] < 0:
            a[x], a[y] = old_x, old_y
            log.append(p)
        else:
            p = p2
            log.append(p2)

        if len(log) > 100:
            log.pop(0)
        if len(log) == 100 and all(i == p for i in log):
            break
    return int(form(a))


def solve():
    ans = 0
    for m in range(2, 16):
        ans += slow(m)
    return ans


epsilon = 10 ** -5
# print(form([1,1]))1
#
# print(form([.9,1.1]))
print('ans =', solve())
# print(time.time() - st, 's')
