from math import floor, ceil, sqrt
import time

st = time.time()
epsilon = pow(10, -10)
alpha = pow(10, -5)
X, Y, R = 1 / 4, 1 / 2, 1 / 4
max_dig = 8

def s(x):
    return min(ceil(x) - x, x - floor(x))


def b_curve(x):
    n = 0
    y = 0
    while True:
        two_n = pow(2, n)
        val = s(two_n * x) / two_n
        if val < epsilon:
            break
        y += val
        n += 1
    return y


def in_circle(x, y, r, x1, y1):
    return (x - x1) ** 2 + (y - y1) ** 2 - r * r < 0


def bino(l, h):
    while h - l > alpha:
        x = (l + h) / 2
        y = b_curve(x)
        if in_circle(X, Y, R, x, y):
            h = x
        else:
            l = x

    return l

def circle_y(x):
    return Y - sqrt(R*R-pow(X-x,2))
def integrate(start, end):
    i = start
    ans = 0
    while i < end:
        y = b_curve(i)
        # print(y,circle_y(i))
        area = alpha*(y-circle_y(i))
        ans+=area
        i += alpha
    return ans

def solve():
    ans = 0
    start = bino(0, X)
    return round(integrate(start, 1 / 2),max_dig)


print('ans = ', solve())
# print(circle_y(0.25))
print(time.time() - st, 's')
