import time
import euler
from math import sqrt

st = time.time()
lim = [2, 9, 81, 4375, 9801, 123201, 336141, 11859211, 11859211, 177182721, 1611308700, 3463200000, 63927525376,
       421138799640, 1109496723126, 1453579866025, 20628591204481, 31887350832897, 31887350832897, 119089041053697]


def is_47_smooth(num):
    for p in primes:
        while num % p == 0:
            num //= p
        if num == 1:
            return True
    # print(num)
    return num <= PRIME_LIM


def is_triangle_number(num):
    x1 = int(sqrt(num * 2))
    if num == x1 * (x1 + 1) // 2:
        return x1
    return 0


def test():
    ans = 0
    for n in range(1, 10 ** 7):
        num = n * (n + 1) // 2
        if num > LIM:
            break
        if is_47_smooth(num):
            ans += n
    return ans


def solve():
    stack = {1}
    ans = 0
    while primes:
        p = primes.pop()
        stack2 = set()
        for i in range(1, LIM):
            pi = p ** i
            if pi > LIM:
                break

            for x in stack:
                pix = pi * x
                if pix <= LIM:
                    stack2.add(pix)
        stack |= stack2
    for i in stack:
        if i+1 in stack:
            ans+=i
    # print(len(stack))
    return ans


PRIME_LIM = 47
primes = euler.list_primes(PRIME_LIM)
LIM = lim[len(primes) - 1]
# LIM = 1453579866025
print('ans = ', solve())
# print(is_47_smooth(2491))
print(time.time() - st, 's')
