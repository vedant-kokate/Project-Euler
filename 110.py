import time
import itertools
import euler
import numpy as np
from math import sqrt
st = time.time()
lim = 4*10**6
prime_num = 12
base = 4
def solve():
    prime = euler.list_primes(100)[:prime_num][::-1]
    ans= 10**100
    for i in range(1,len(prime)**(prime_num+1)):
        s = np.base_repr(i, base=base) + ""
        s = "0"*(prime_num-len(s))+s
        if len(s)>prime_num:
            break
        factors = 1
        num = 1
        for k,v in enumerate(s):
            factors *= int(v)*2+1
            # if k>=len(prime):
            #     # print(s)
            num *= prime[k]**(int(v)*2)
        if (factors+ 1) // 2>lim and num<ans:
            print(s,factors,sqrt(num))
            ans = num
    return sqrt(ans)

print('ans =', solve())
print(time.time() - st, 's')
