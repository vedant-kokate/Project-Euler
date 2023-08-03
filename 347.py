import time

import euler

st = time.time()
lim = 10 ** 7


def solve():
    prime = euler.list_primes(lim // 2)
    # print(prime)
    sqrt_limit = euler.sqrt(lim)
    ans = 0
    for i, p in enumerate(prime):
        if p > sqrt_limit:
            break

        for j in range(i + 1, len(prime)):
            q = prime[j]
            pq = p * q
            if pq>lim:
                break
            max_reach = lim // pq
            multuplier = 1
            # if p==2 and q==29:
            #     print(max_reach)
            while multuplier * p <= max_reach:
                multuplier *= p
            max_mutiplier = multuplier
            while multuplier % p == 0:
                multuplier //= p
                while multuplier * q <= max_reach:
                    multuplier *= q
                max_mutiplier = max(max_mutiplier, multuplier)
            # print(p, q, max_mutiplier * pq)
            ans += max_mutiplier * pq
    return ans


print('ans =', solve())
print(time.time() - st, 's')
