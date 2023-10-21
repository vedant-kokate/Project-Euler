import time
import euler

st = time.time()
lim = 10 ** 9


def dfs():
    stack = {1}

    while primes:
        p = primes.pop()
        stack2 = set()
        for i in range(1, lim):
            pi = p ** i
            if pi > lim:
                break

            for x in stack:
                pix = pi * x
                if pix <= lim:
                    stack2.add(pix)
            # print(stack2,p)
        stack |= stack2
    # print(stack)
    return len(stack)


def solve():
    return dfs()


ans = 0
primes = euler.list_primes(100)
print('ans =', solve())
# print(form(-0.46, 1, 1))
print(time.time() - st, 's')
