
# Solved in google collab

import numpy as np


def sieve_eratosthenes(n):
    is_prime = np.ones(n, dtype=bool)
    is_prime[:2] = 0  # 0 and 1 are not prime

    for candidate in range(2, int(np.sqrt(n)) + 1):
        if is_prime[candidate]:
            is_prime[candidate ** 2::candidate] = 0

    return np.nonzero(is_prime)[0]


n = 2 * 10 ** 9
primes = sieve_eratosthenes(n)
print(len(primes))
def prime_factors_with_exponent(n):
    factors = []
    d = 2
    while n > 1:
        count = 0
        while n % d == 0:
            count += 1
            n /= d
        if count > 0:
            factors.append([d, count])
        d = d + 1
        if d * d > n:
            if n > 1:
                factors.append([int(n), 1])
            break
    return factors

def is_practical(x):
    pf = prime_factors_with_exponent(x)
    if pf[0][0] != 2: #Start by checking is 2 is a prime factor for completeness
        return False
    if len(pf) == 1: #This means 2 is the only prime factor so x = 2^e => it is practical
        return True
    for x in range(1, len(pf)):
        p1, e1 = pf[x]
        total = 1
        for y in range(x):
            p, e = pf[y]
            if p != p1:
                total *= ((pow(p, (e + 1)) - 1)//(p - 1))
                #This is calculating the sum of divisors of x without the prime factor, p1
        if p1 > total + 1:
            #If a single prime fails the condition, then x is not practical
            return False
    return True

def solve():
  ans = []
  for i in range(3,len(primes)):
    p1,p2,p3,p4 = primes[i-3],primes[i-2],primes[i-1],primes[i]
    if p2-p1==6 and p3-p2==6 and p4-p3==6:
      n = p4-9
      if all(is_practical(x) for x in [n-8,n-4,n,n+4,n+8]):
        ans.append(n)
        print(n)
        if len(ans)==4:
          return ans

ans = solve()
# 219869980
# 312501820
# 360613700
# 1146521020
print(sum(ans))
# 2039506520