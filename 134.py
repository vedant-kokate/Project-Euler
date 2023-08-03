import itertools

import euler
import time

st = time.time()
lim = 10 ** 6+3

def solve2():
    primes = euler.list_primes(lim)
    total=0
    for x in range(2,len(primes) - 1):
        p1 = primes[x]
        p2 = primes[x + 1]


        k = 10 ** len(str(p1))
        m = -p1 * pow(k, p2 - 2, p2) % p2
        total += (m * k + p1)
    return total

def solve():
    a = []
    ans = 0
    prime = euler.list_primes(lim)
    for i in range(len(prime) - 1):
        n, m = prime[i], prime[i + 1]
        if n<5:
            continue
        num = ''
        for p in range(1, len(str(n)) + 1):
            for dig in range(10):
                new_num = int(str(dig) + num)
                if (new_num * m) % (10 ** p) == n % (10 ** p):
                    break
            num = str(dig) + num
            # print('num',num)
        k = 10 ** len(str(n))
        # print(pow(2,3))
        M = -n * pow(k, m - 2, m) % m
        num2 = M * k + n
        if num2 != int(num)*m:
            print('fail', n, m, int(num)*m,num2)
            return
        if (int(num) * m) % (10 ** len(str(n))) != n:
            print(n, m, num)
            return
        ans += int(num) * m
        a.append((n, m, num))
        # print(int(num) * m, n, m, num)
    return ans


print('ans =', solve())
# print(pow(10,2,7))
print(time.time() - st, 's')
