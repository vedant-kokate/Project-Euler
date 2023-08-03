import euler
import math
import time

st = time.time()
lim = 10 ** 6 +1


def solve():
    prime = euler.list_primality(lim)
    ans = 0
    for i in range(1,lim):
        val = i**3-(i-1)**3
        if val < lim and prime[val]:
            ans+=1
    return ans

print('ans =', solve())
print(time.time() - st, 's')
