import time
from math import sqrt

st = time.time()
lim = 10 ** 9


def two_point_tp_line(x1, y1, x2, y2):
    m = (y1 - y2) / (x1 - x2)
    c = get_c_from_line(m, x1, y1)
    return m, c


def get_roots(a, b, c):
    d = b * b - 4 * a * c
    if d < 0:
        return None, None
    d = sqrt(d)
    x1 = (-b + d) / (2 * a)
    x2 = (-b - d) / (2 * a)
    return x1, x2


def get_y_from_line(m, c, x):
    y = m * x + c
    return y


def get_c_from_line(m, x1, y1):
    return y1 - m * x1


def line_slope_intersection(m, c, a, b):
    x_a, x_b, x_c = ((a ** 2) * (m ** 2) + b ** 2), 2 * (a ** 2) * m * c, (a ** 2) * (c ** 2 - b ** 2)
    x1, x2 = get_roots(x_a, x_b, x_c)
    y1, y2 = get_y_from_line(m, c, x1), get_y_from_line(m, c, x2)

    return x1, y1, x2, y2


def get_tangent_eclipse(a, b, x1, y1):
    m = -(b * b * x1 / (a * a * y1))
    c = y1 - m * x1
    return m, c


def get_reflection_slope(m1, m2):
    x = abs((m1 - m2) / (1 + m1 * m2))
    return (m2 - x) / (m2 * x + 1)


def similar(last_point, x2, y2):
    x1, y1 = last_point
    if abs(x1 - x2) <= 0.0001 and abs(y1 - y2) <= 0.0001:
        return True
    return False


def solve(a, b):
    x1, y1 = 0.007107316949965852, 9.99998989720405
    last_point = [x1, y1]
    m, c = two_point_tp_line(0, 10.1, 1.4, -9.6)
    for _ in range(3500):
        x1, y1, x2, y2 = line_slope_intersection(m, c, a, b)
        # print(f"{_} x1: {x1} y1: {y1} x2: {x2} y2: {y2}")
        if similar(last_point,x1,y1):
            x1, y1 = x2, y2
        last_point = [x1,y1]
        # print(f"{_} x1: {x1} y1: {y1}")
        if -0.01 <= x1 <= 0.01 and y1 > 0:
            return _

        t_m, t_c = get_tangent_eclipse(a, b, x1, y1)
        # print(f"{len(points)} t_m: {t_m} t_c: {t_c}")
        m = get_reflection_slope(m, t_m)
        c = get_c_from_line(m, x1, y1)
        # print(f"{_} m: {m} c: {c}")
    # for i in range


# a, b = 5, 10
# print(line_slope_intersection(m, c, a, b))
print('ans =', solve(5, 10))
# print(pow(10,2,7))
print(time.time() - st, 's')
