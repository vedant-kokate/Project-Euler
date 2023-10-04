import time
from math import pi

st = time.time()


def form(x):
    g = 9.81
    h = 100
    v = 20
    return v * v / 2 / g - g * x * x / 2 / v / v + h


def volume_integration(form):
    step = 0.00001
    x = 0
    ans = 0
    avg_vol = 0.0001
    last_y = 0
    while True:
        print(x)
        y = form(x)
        if y <= 0:
            break
        vol = pi * y * x * x * abs(y - last_y)
        if vol > avg_vol:
            step /= 2
        else:
            step *= 2
        ans += vol
        x += step
        last_y = y
    return ans


def solve():
    h=100
    v=20
    g=9.81
#     xa+b
    a = g/(2*v*v)
    b = v*v/2/g+h
    return round(pi/2*b*b/a,4)


# print(form(90))
print('ans =', solve())
print(time.time() - st, 's')
