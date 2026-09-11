from decimal import Decimal, getcontext, InvalidOperation
from time import time

start_time = time()

getcontext().prec = 12
M = 400
N = M//2
EPS = Decimal(1).scaleb(-10)  # convergence threshold


def f(x):
    x = Decimal(x)
    val = (Decimal(1) - x * x)
    if val <= 0:
        return None  # signal invalid
    return val.sqrt()


def get_x3(x1, x2):
    x1 = Decimal(x1)
    x2 = Decimal(x2)
    fx1, fx2 = f(x1), f(x2)
    if fx1 is None or fx2 is None:
        return None
    return x2 + fx2 * (fx1 - fx2) / x2


def get_seq(x1):
    x1 = Decimal(x1)
    a = [Decimal(0), x1]

    for i in range(1, N + 1):
        x1, x2 = a[-2], a[-1]
        x3 = get_x3(x1, x2)
        if x3 is None:
            return None
        a.append(x3)
    return a


def area(a):
    ans = Decimal(0)
    for i in range(N+1):
        xi, xi_plus_1 = a[i], a[i + 1]
        ans += (xi_plus_1 - xi) * f(xi)
    return ans * 4


low, high = Decimal(0), Decimal(1)
while high - low > EPS:
    mid = (low + high) / 2
    seq = get_seq(mid)
    if seq is None or seq[-1] > 1:
        high = mid
    else:
        low = mid

mid = (low + high) / 2
seq = get_seq(mid)
ans = area(seq)
print("Area of the region: {}".format(ans.quantize(Decimal("0.0000000001"))))
print("Time taken: {} seconds".format(time() - start_time))
print("=====================================")