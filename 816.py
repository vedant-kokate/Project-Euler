import time

st = time.time()
from math import sqrt


def point_genrate(n):
    s = 290797
    mod = 50515093
    points = []
    while len(points) < n:
        s2 = pow(s, 2, mod)
        points.append((s, s2))
        s = pow(s2, 2, mod)
    return points


def dist(p1, p2):
    return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def divide(points):
    n = len(points)
    if n == 2:
        return dist(points[0], points[1])
    if n == 3:
        return min(dist(points[0], points[1]), dist(points[1], points[2]), dist(points[2], points[0]))

    mid = n // 2
    dl = divide(points[:mid])
    dr = divide(points[mid:])
    d = min(dl, dr)
    # print('before', n, d, dl, dr, points)
    mid_x = points[mid][0]
    s = [p for p in points if abs(p[0] - mid_x) < d]
    for i in range(len(s)):
        for j in range(i + 1, min(i + 8, len(s))):
            d = min(d, dist(points[i], points[j]))
    # print('after', d, points)
    return d


def solve():
    points = point_genrate(LIM)
    points.sort()
    print('POINTS GENERATED')
    return divide(points)


LIM = 2*10**6
print('ans = ', solve())
# print(dist((290797, 629527), (3245540, 21669054)))
print(time.time() - st, 's')
