import time
import euler
from math import sqrt

st = time.time()
TOTAL_DIGITS = 10


def is_prime(n):
    end = int(sqrt(n)) + 1
    for p in primes:
        if p > end:
            break
        if n % p == 0:
            return False
    return True


def to_9_base(n, l):
    a = []
    while n:
        d = n % 9
        a.append(d)
        n //= 9
    a = a[::-1]
    if len(a) < l:
        a = [0] * (l - len(a)) + a
    return a


def solve():
    ans = set()
    for dig in range(10):
        for reps in range(TOTAL_DIGITS - 1, -1, -1):
            d_sum = set()
            pre = [dig] * reps
            for suffix_int in range(9 ** (TOTAL_DIGITS - reps)):

                suff_l = to_9_base(suffix_int, TOTAL_DIGITS - reps)
                flag = False
                # print('before',dig, reps, suff_l, suffix_int)
                for i in range(len(suff_l)):
                    if suff_l[i] == 9:
                        flag = True
                        break
                    if suff_l[i] >= dig:
                        suff_l[i] += 1
                if flag:
                    continue
                # print(dig, reps, suff_l, suffix_int)
                num = pre + suff_l
                # print(num)
                num.sort()
                while True:
                    if num[0] > 0:
                        num_int = int("".join(map(str, num)))
                        if is_prime(num_int):
                            # print(dig, reps, num_int)
                            d_sum |= {num_int}

                    if not euler.next_permutation(num):
                        break
            if len(d_sum) > 0:
                # print(dig, reps)
                ans |= d_sum
                break
    return sum(ans)


primes = euler.list_primes(int(sqrt(10 ** TOTAL_DIGITS)) + 2)

print('ans =', solve())
print(time.time() - st, 's')
