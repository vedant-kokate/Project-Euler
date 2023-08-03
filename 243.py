import time

import euler

st = time.time()
lim = 10 ** 5
check = 15499 / 94744


# check = 4 / 10


def solve():
    prime = euler.get_prime_list(100)
    num, denom = 1, 1
    for i in prime:
        num *= (i - 1)
        denom *= i
        if num / denom < check:
            for b in range(2, 10 ** 6):
                val = num * b / (denom * b - 1)
                if val < check:
                    return b * denom


print('ans =', solve())
print(time.time() - st, 's')
