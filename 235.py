import time
from decimal import Decimal as D

st = time.time()
N = 5000
target = -600_000_000_000

def form(r):
    ans = 0
    for k in range(1, N + 1):
        val = (900 - 3 * k) * r ** (k - 1)
        ans += val
    return ans


def solve():
    l = D(1.0)
    h = D(2.0)
    while h - l > 10 ** -14:
        # print(h,l)
        m = (l + h) / 2
        x = form(m)
        if x>target:
            l=m
        else:
            h=m
    return round(h,12)


# print(form(1))
print('ans =', solve())
# print(get_var(2,3))
print(time.time() - st, 's')
