from math import sqrt, pi
from collections import deque
import time

st = time.time()
lim = 10 ** 6 + 3
lim = 10
round_dig = 8

def form(k1, k2, k3):
    return k1 + k2 + k3 + 2 * (sqrt(k1 * k2 + k1 * k3 + k2 * k3))


def area(k):
    r = 1 / k
    return (pi) * r * r
def solve():
    inner_k = 1
    outter_k = 3 - 2 * sqrt((3))
    stack = [(inner_k, inner_k, outter_k, 0)] * 3 + [(inner_k, inner_k, inner_k, 0)]
    stack = deque(stack)
    d = 0
    circle_area = area(-outter_k)
    inner_area = area(inner_k) * 3
    while stack:
        k1, k2, k3, d = stack.popleft()
        if d >= lim:
            continue
        d += 1
        k4 = form(k1, k2, k3)
        inner_area += area(k4)

        stack.append((k4, k1, k2, d))
        stack.append((k4, k1, k3, d))
        stack.append((k4, k3, k2, d))

    return round((circle_area - inner_area) / circle_area,round_dig)


print('ans =', solve())
# print(form(-0.46, 1, 1))
print(time.time() - st, 's')
