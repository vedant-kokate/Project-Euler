import euler
import math
import time

st = time.time()
lim = 10**5


def solve():
    prime = euler.list_primes(lim)
    # print(prime)
    ans = []
    for p in prime:
        flag = True
        for i in range(1, 100):
            if pow(10, 10 ** i, p * 9) == 1:
                flag = False
                break
        if flag:
            ans.append(p)
    return sum(ans)


print('ans =', solve())
print(time.time() - st, 's')
