import time

st = time.time()


def bino(n, r):
    return fact(n) // fact(n - r) // fact(r)


def fact(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f


n = 100
# ans = bino(n + 9, n) - 1
ans = bino(n + 9, n) - 1 + bino(n + 10, n) - (n + 1) - 9 * n
print('ans =', ans)
print(time.time() - st, 's')
