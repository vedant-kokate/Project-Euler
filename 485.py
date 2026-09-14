from array import array
from time import time
from math import isqrt

start = time()

U = 10**8
K = 10**5

spf = array('H', [0]) * (U + 1)
d = array('H', [0]) * (U + 1)
print("Arrays initialized:", time() - start)
limit = isqrt(U)
for p in range(2, limit + 1):
    if spf[p] == 0:
        for n in range(p * p, U + 1, p):
            spf[n] = p
print("SPF:", time() - start)
d[1] = 1
for i in range(2, U + 1):
    if spf[i] == 0:
        d[i] = 2
    else:
        p = spf[i]
        m = i // p
        count = 1
        while m % p == 0:
            m //= p
            count += 1
        d[i] = d[m] * (count + 1)
print("Divisor counts:", time() - start)

num_count = {}
for i in range(1, K + 1):
    if d[i] not in num_count:
        num_count[d[i]] = 0
    num_count[d[i]] += 1
m = max(num_count)

result = m

for i in range(1, U - K + 1):
    add = d[i + K]
    remove = d[i]
    if add not in num_count:
        num_count[add] = 0
    num_count[add] += 1
    if add > m:
        m = add

    if remove in num_count:
        num_count[remove] -= 1
        if num_count[remove] == 0:
            del num_count[remove]
            if m == remove:
                m = max(num_count)
    result += m
    
print(f"Result: {result} (in {time() - start:.2f}s)")

