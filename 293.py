import euler
import time
import sys

sys.setrecursionlimit(10 ** 6)

st = time.time()
LIM = 10 ** 9 + 1


def get_num(prime, l):
    num = 1
    for i in range(len(l)):
        num *= prime[i] ** l[i]
    return num


def dfs(prime, l, num):
    p = get_num(prime, l)
    if p * num > LIM:
        for i in range(len(l)):
            if l[i] != 0:
                l[i] = 0
                if i + 1 < len(l):
                    l[i + 1] += 1
                    return dfs(prime, l, num)
                else:
                    return []
    l[0] += 1
    return [p * num] + dfs(prime, l, num)


def get_M(num):
    for i in range(3, LIM, 2):
        num2 = num + i
        if euler.is_prime(num2):
            return i


def solve():
    prime = euler.list_primes(25)
    num = 1
    nums = []
    for i in range(len(prime)):
        num *= prime[i]
        nums += dfs(prime, [0] * (i + 1), num)

    # print(len(nums))
    nums.sort()
    ms = set()
    ans = 0
    for num in nums:
        if num > LIM:
            print(num, LIM)

        m = get_M(num)
        ms.add(m)

    return sum(ms)

print('ans =', solve())
# print(get_M(630))
print(time.time() - st, 's')
