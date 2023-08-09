import math
from math import floor, ceil, sqrt, factorial
import time
DIGIT_LIMIT = 12
import euler

st = time.time()

# Number of people
N = 100
# People fixed at
X = 3
Y = 22


def C(n, r):
    return factorial(n) / factorial(n - r) / factorial(r)


def solve():
    d = [1, 0]
    while len(d) <= N:
        d.append((len(d) - 1) * (d[-1] + d[-2]))

    return round(sum(d[N-X-i] * C(N-X-Y,i) for i in range(75)) * C(25, 3) / factorial(N),DIGIT_LIMIT)



print('ans = ', solve())
# print(circle_y(0.25))
print(time.time() - st, 's')
