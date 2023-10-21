import itertools
import time

st = time.time()


def d(k, n):
    return ((10 * pow(10, n - 1, k)) // k) % 10


def get_chain(n):
    mem = {}
    cur = 10
    chain = []
    for i in itertools.count(0):
        if cur in mem:
            break
        mem[cur] = i
        chain.append(cur // n)
        cur %= n
        cur *= 10
    return chain[:mem[cur]], chain[mem[cur]:]
    # print(, )
    # print(mem, cur, )


def solve():
    n = 10 ** 7
    ans = 0
    max_ = 0
    for k in range(1, n + 1):
        ans += d(k,n)
        # pre, recur = get_chain(k)
        # max_ = max(max_, len(recur))
        # n_array = (n - 1 - len(pre)) % (len(recur))
        # ans.append(recur[n_array])
    # print(max_)
    return ans


print('ans = ', solve())
# get_chain(39)
print(time.time() - st, 's')
