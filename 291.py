import time

st = time.time()
import euler
import math
# SOLVED IN COLLAB

def is_prime(x):  # Test if giving value is a prime
    if x <= 1:
        return 0
    elif x <= 3:
        return 1
    elif x % 2 == 0:
        return 0
    else:
        for i in range(3, int(math.sqrt(x)) + 1, 2):
            if x % i == 0:
                return 0
        return 1


def fermat_primality_test(n, tests):
    if n < 10 ** 5:
        return is_prime(n)
    else:
        for x in range(tests):
            if pow(2 * (x + 2), n - 1, n) != 1:
                return 0
        return 1


def solve(s, e):
    # print('started',time.time()-st)
    ans = 0

    for n in range(s, e):
        num = n * n + (n + 1) ** 2
        if num > e:
            break
        if fermat_primality_test(num, 5):
            ans += 1
    return ans, n


a1,n = solve(1,10**10)
a2,n =solve(n,10**11)
a3,n =solve(n,10**12)
a4,n =solve(n,10**13)
a5,n =solve(n,10**14)
a6,n = solve(n,10**15)
a7=solve(n,5*10**15)
print(a1+a2+a3+a4+a5+a6+a7[0])
print(time.time() - st, 's')
