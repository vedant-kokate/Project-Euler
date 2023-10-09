import time

st = time.time()
LIM = 26
fact = [1]
for i in range(1, 27):
    fact.append(fact[-1] * i)


def C(n, r):
    return fact[n] / fact[r] / fact[n - r]


def calc(n):
    ans = 0
    for i in range(1, n):
        left = C(n, i)
        ans += left - 1
    # print(n,ans)
    return ans * 4(26, n)


def solve():
    ans = 0
    for i in range(2, LIM + 1):
        ans = max(ans,calc(i))

    return int(ans)


print('ans =', solve())

print(time.time() - st, 's')
