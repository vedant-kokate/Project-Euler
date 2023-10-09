import time

st = time.time()
LIM = 2560000


def solve():
    f = 1
    for i in range(2, LIM + 1):
        f *= i
        while f % 10 == 0:
            f //= 10
        f %= 10 ** 20
    f %= 10 ** 5
    return f


print('ans =', solve())

print(time.time() - st, 's')
