import time

import euler

st = time.time()
lim = 10**8


def solve():
    prime = euler.list_primes(lim)
    ans=0
    for i in range(lim):
        if not prime[i+1]:
            continue
        flag = True
        for j in range(2, euler.sqrt(lim)):
            if i % j == 0 and not prime[i // j + j]:
                flag = False
                break
        if flag:
            ans += i

    return ans


print('ans =', solve())
print(time.time() - st, 's')
