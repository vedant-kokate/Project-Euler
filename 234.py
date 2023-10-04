import euler
import time
from math import ceil, sqrt

st = time.time()

LIM = 999966663333


def form(n, a, d):
    return n * (2 * a + (n - 1) * d)//2


def get_var(pl, ph):
    # print('pl ph',pl,ph)
    l = pl * pl
    h = min(LIM, ph * ph)
    pl_a = pl * (pl + 1)
    pl_n = (h // pl * pl - pl_a) // pl + 1

    pl_sum = form(pl_n, pl_a, pl)
    # print(pl_a, pl_n, pl,pl_sum)
    ph_a = (l // ph + 1) * ph
    if h == ph * ph:
        ph_n = (ph * (ph - 1) - ph_a) // ph + 1
    else:
        ph_n = (LIM // ph * ph - ph_a) // ph + 1

    ph_sum = form(ph_n, ph_a, ph)
    # print(ph_a, ph_n, ph, ph_sum)
    # print(ph_sum + pl_sum - ph * pl * 2)
    # print("============================")
    ans = ph_sum + pl_sum
    if pl*ph<=LIM:
        ans-=ph * pl * 2
    return ans


def solve():
    primes = euler.list_primes(ceil(sqrt(LIM))+1000)
    while primes[-1]*primes[-1]>LIM:
        temp = primes.pop()
    primes.append(temp)
    # print(primes)


    ans = 0
    for i in range(1, len(primes)):
        pl = primes[i - 1]
        if pl*pl>LIM:
            break
        ph = primes[i]
        ans += get_var(pl, ph)
    return ans

print('ans =', solve())
# print(get_var(2,3))
print(time.time() - st, 's')
