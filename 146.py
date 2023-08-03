import itertools
import math

import euler
import time

st = time.time()
lim = 150 * 10 ** 6
inc = [1, 3, 7, 9, 13, 27]
oth = set(range(1,inc[-1])) - set(inc)
primes = euler.list_primes(lim)
time_cal={0}
def solve():
    print("Stared solving.... at",time.time()-st,'seconds')
    ans = 0
    # return len(primes)
    for i in range(10,lim,10):
        # print(i, all(is_prime(i + k) for k in inc), any(is_prime(i+k) for k in oth))
        curr_time = int(float(time.time() - st))
        if curr_time%10==0 and curr_time not in time_cal:
            print(curr_time,'sec i=',i)
            time_cal.add(curr_time)
        var = [i*i+k for k in inc]
        if any((x != p and x % p == 0)
               for p in primes
               for x in var):
            continue
        if any(is_prime(i*i+k) for k in oth):
            continue

        if any(not is_prime(i*i+k) for k in inc):
            continue
        ans += i
            # print(i)
    return ans


def is_prime(n):
    end = int(math.sqrt(n))
    for p in primes:
        if p > end:
            break
        if n % p == 0:
            return False
    return True
print('ans =', solve())
# print(pow(10,2,7))
print(time.time() - st, 's')
