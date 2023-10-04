import time

st = time.time()


def solve():
    A = 1777
    B = 1855
    mod = 10 ** 8
    res = 1
    last = 0
    for b in range(B, -1, -1):
        res = pow(A, res, mod)
        # if res == last:
        #     return res
        last = res

    return res
print('ans =', solve())
print(time.time() - st, 's')
