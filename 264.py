import time
from math import sqrt, floor, ceil
from itertools import combinations

st = time.time()
lim = 10 ** 5
mem = {}
p_max = 0
round_dig = 10


# from
def check_sq(x):
    return ceil(x) == floor(x)

def print_anomaly(l,val):
    print(l)
    print("ANOMALY",val)
    print("====================")
    exit()

def anomaly_detection(l):
    r = l[0][0] ** 2 + l[0][1] ** 2

    if any((a ** 2 + b ** 2) // 1 % 5 != 0 for a, b in l):
        print_anomaly(l,'1')



    if any((a ** 2 + b ** 2) != r for a, b in l):
        print_anomaly(l,'2')

    t1, t2, t3 = l
    # print(t1)
    x1, y1 = t1
    x2, y2 = t2
    x3, y3 = t3
    if x1 + x2 + x3 != 5 or y1 + y2 + y3 != 0:
        print_anomaly(l,'3')

    if (x1 - 5) * (x3 - x2) != y1 * (y2 - y3):
        print_anomaly(l,'4')

    if (x2 - 5) * (x3 - x1) != y2 * (y1 - y3):
        print_anomaly(l,'5')

    if (x3 - 5) * (x1 - x2) != y3 * (y2 - y1):
        print_anomaly(l,'6')

    if calc_perimeter(l) >= 10 ** 5:
        print_anomaly(l,'7')


def calc_perimeter(l):
    p = 0
    for x, y in list(combinations(l, 2)):
        x1, y1 = x
        x2, y2 = y
        p += sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return p


def perimeter_triangle(x1, y1, x2, y2, x3, y3):
    l = [(int(x1), int(y1)), (int(x2), int(y2)), (int(x3), int(y3))]
    l.sort(key=lambda x: (x[0], x[1]))

    if str(l) in mem:
        return 0
    p = calc_perimeter(l)

    global p_max
    p_max = max(p_max, p)
    if p > lim:
        return 0
    mem[str(l)] = True
    anomaly_detection(l)

    global ans
    ans += p
    return p


def special_1(x1, y1):
    x2 = x3 = (5 + x1) / 2
    y2 = y3 = sqrt((3 * x1 * x1 - 25 - 10 * x1) / 4)
    y3 = -y3
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2) + sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2) + sqrt(
        (x1 - x3) ** 2 + (y1 - y3) ** 2)

    y2 = round(y2, round_dig)
    x2 = round(x2, round_dig)
    x3 = round(x3, round_dig)
    y3 = round(y3, round_dig)
    if (x3, y3) not in [(x1, y1), (x2, y2)] and (x1, y1) != (x2, y2):
        return perimeter_triangle(x1, y1, x2, y2, x3, y3)


def special_2(x1, y1):
    y2 = y3 = -y1 / 2
    x2 = sqrt(25 + y1 * y1 - y2 * y2)
    x3 = -x2

    y2 = round(y2, round_dig)
    x2 = round(x2, round_dig)
    x3 = round(x3, round_dig)
    y3 = round(y3, round_dig)
    if not check_sq(y2) or not check_sq(x2):
        return 0
    if (x3, y3) not in [(x1, y1), (x2, y2)] and (x1, y1) != (x2, y2):
        return perimeter_triangle(x1, y1, x2, y2, x3, y3)


def trial(x1, y1):
    if y1 == 0:
        return special_1(x1, y1)
    if x1 == 5:
        return special_2(x1, y1)

    m = y1 / (5 - x1)
    c = (y1 * (1 + m * m)) / (-2 * m * m)
    t = -c * m
    d = 4 * m * m * t * t - 4 * (1 + m * m) * (t * t - x1 * x1 - y1 * y1)

    if d < 0:
        return 0
    d = sqrt(d)
    y2 = round((-2 * m * t + d) / (2 * (1 + m * m)), round_dig)

    if not check_sq(y2):
        return 0
    x2 = round((y2 - c) * m, round_dig)

    if not check_sq(x2):
        return 0
    x3 = 5 - x1 - x2
    y3 = -y1 - y2
    if (x3, y3) not in [(x1, y1), (x2, y2)] and (x1, y1) != (x2, y2):
        return perimeter_triangle(x1, y1, x2, y2, x3, y3)
    return 0


# solve [//math:x1^2+y1^2 = x2^2+y2^2//],[//math:x1^2+y1^2 = x3^2+y3^2//],[//math:x2^2+y2^2 = x3^2+y3^2//],[//math:y1+y2+y3=0//],[//math:x1+x2+x3=5//]
def all_poss(x1, y1):
    return trial(x1, y1) + trial(-x1, y1)


def get_min_p(r):
    x2, y2 = r, 0
    x1 = x3 = (5 + r) / 2
    y1 = y3 = sqrt((3 * r * r - 25 - 10 * r) / 4)
    y3 = -y3

    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2) + sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2) + sqrt(
        (x1 - x3) ** 2 + (y1 - y3) ** 2)


def solve():
    N = 10 ** 3

    for x1 in range(1, N):
        if x1 % 10 ** 2 == 0:
            print(x1 * 100 / N, '%', time.time() - st, 's', p_max)
        if x1 > LIM:
            break
        for y1 in range(1, N):
            all_poss(x1, y1)

    print('mem', len(mem), p_max)
    return ans


def solve2():
    N = 5 * 10 ** 4
    pair = [(1, 2), (1, 8), (0, 5), (2, 9), (3, 4), (3, 6), (4, 7), (6, 7), (8, 9)]
    for p1, p2 in pair:
        print(p1, p2,ans,len(mem),p_max,time.time()-st,'s')
        for x1 in range(p1, N, 10):
            if x1 > LIM:
                break
            for y1 in range(p2, min(N, int(sqrt(LIM * LIM - x1 * x1))), 10):
                all_poss(x1, y1)
                all_poss(y1, x1)

    print(len(mem), p_max)
    return ans


main_save = []

l = 1
h = 10 ** 6
while l < h:
    m = (l + h) // 2
    x = get_min_p(m)
    if x < lim:
        l = m + 1
    else:
        h = m
LIM = h + 100
ans = 0
print('ans =', solve2())
print(time.time() - st, 's')

