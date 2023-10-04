import time
import sys

sys.setrecursionlimit(10 ** 7)
st = time.time()
LIM = 10
from math import sqrt, ceil, floor, pi


# class Point:
#     def __init__(self, x, y, next=None, prev=None):
#         self.x = x
#         self.y = y
#         self.next = next
#         self.prev = prev
#
#
# def dist(p1, p2):
#     x1, y1 = p1.x, p1.y
#     x2, y2 = p2.x, p2.y
#     return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
#
#
# def traingle_area_perimeter(p1, p2, p3):
#     x1, y1 = p1.x, p1.y
#     x2, y2 = p2.x, p2.y
#     x3, y3 = p3.x, p3.y
#     area = 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
#
#     perimeter = dist(p1, p2) + dist(p2, p3) - dist(p1, p3)
#     return area, perimeter
#
#
# def form(x):
#     s = 500
#     a = s * s - x * x * 2
#     p = 4 * s - 8 * x + x * sqrt(2) * 4
#     return a / p
#
#
# def change(p1, p2, p3, diff):
#     a, p = traingle_area_perimeter(p1, p2, p3)
#     if a == 0:
#         return False, -1, -1
#
#     p2.x, p2.y = p2.x - diff[0], p2.y - diff[1]
#     new_a, new_p = traingle_area_perimeter(p1, p2, p3)
#
#     if a - new_a < p - new_p:
#         if same_point(p1, p2) or same_point(p3, p2):
#             p1.next = p3
#         return True, a - new_a, p - new_p
#     return False, -1, -1
#
#
# def same_point(p1, p2):
#     return p1.x == p2.x and p1.y == p2.y
#
#
# def dfs(head, area, perimeter, d):
#     # if d>5:
#     #     return
#
#     print_points(head)
#
#     if (area, perimeter, d) in mem:
#         return
#     mem[(area, perimeter, d)] = True
#     cur = head
#     if cur is None or cur.next is None:
#         return
#     while cur.next.next is not None:
#         p1 = cur
#         p2 = cur.next
#         p3 = p2.next
#
#         save = (p2.x, p2.y)
#
#         flag, a, p = change(p1, p2, p3, (1, 0))
#         if flag:
#             dfs(head, area + a, perimeter + p, d + 1)
#         p2.x, p2.y = save
#         p1.next = p2
#
#         flag, a, p = change(p1, p2, p3, (0, 1))
#         if flag:
#             dfs(head, area + a, perimeter + p, d + 1)
#         p2.x, p2.y = save
#         p1.next = p2
#
#         cur = cur.next
#
#
# def print_points(head):
#     cur = head
#     # print(f"{cur.x},{cur.y}", end=' ')
#     # temp =[]
#     while cur is not None:
#         # temp.append((cur.x,cur.y))
#         # if not(cur.x==LIM or cur.y==LIM):
#         print(f"{cur.x},{cur.y}", end=' ')
#         cur = cur.next
#     # print(f"{LIM},{0}", end=' ')
#     print()
#     # for i in range(1,len(temp)):
#     #     if temp[i][0]==temp[i-1][0] or temp[i][1]==temp[i-1][1]:
#     #         continue
#     #     print(f"{temp[i]}", end=' ')
#
#
# def slope_match(p1, p2, p3):
#     return (p1.y - p2.y) * (p3.x - p2.x) == (p3.y - p2.y) * (p1.x - p2.x)
#
#
#
#
# def populate(p1, p2):
#     if p1.y == p2.y:
#         for i in range(p1.x + 1, p2.x):
#             p1.next = Point(i, p1.y, prev=p1)
#             p1 = p1.next
#
#         p1.next = p2
#         return
#     if p1.x == p2.x:
#
#         for i in range(p1.y - 1, p2.y, -1):
#             p1.next = Point(p1.x, i, prev=p1)
#             p1 = p1.next
#         p1.next = p2
#         return
#     m = (p1.y - p2.y) / (p1.x - p2.x)
#     c = p1.y - m * p1.x
#     for x in range(p1.x + 1, p2.x):
#         y = m * x + c
#         if check_sq(y):
#             p1.next = Point(x, int(y), prev=p1)
#             p1 = p1.next
#     p1.next = p2
#     return p2
#
#
# def same_side(p1, p2, p3, diff):
#     side_1 = (p2.x - p1.x) * (p1.y - p3.y) - (p2.y - p1.y) * (p1.x - p3.x)
#     # print(side_1, (p2.x - p1.x) * (p1.y - p3.y), (p2.y - p1.y) * (p1.x - p3.x))
#     side_2 = (p2.x - p1.x - diff[0]) * (p1.y - p2.y) - (p2.y - p1.y - diff[1]) * (p1.x - p3.x)
#     # print(side_2, (p3.x - p1.x - diff[0]) * (p1.y - p2.y), (p3.y - p1.y - diff[1]) * (p1.x - p2.x))
#     return side_2 * side_1 > 0
#
#
# def trial(head):
#     area = LIM * LIM * 4
#     perimeter = LIM * 8
#     while True:
#         flag = True
#         cur = head
#         choice = (10 ** 9, 0, 0, 0, 0, 0, None)
#         while cur.next.next is not None:
#             p1 = cur
#             p2 = cur.next
#             p3 = p2.next
#             # if p2.y<p2.x:
#             #     break
#             # print(p1.x,p1.y,p2.x,p2.y,p3.x,p3.y)
#             if not slope_match(p1, p2, p3):
#                 a, p = traingle_area_perimeter(p1, p2, p3)
#                 # print(round(a,2),round(p,2),round(a/p,2),round(area/perimeter,2),p2.x,p2.y)
#                 ratio = a / p
#                 if p >= 0 and ratio < area / perimeter and ratio < choice[0]:
#                     choice = (ratio, a, p, p1, p2, p3, None)
#                     flag = False
#                 for diff in [(1, 0), (0, 1)]:
#                     if p2.x - diff[0] != p1.x and p2.y - diff[1] != p1.y and same_side(p1, p2, p3, diff):
#                         p1.x -= 1
#                         par_a, par_p = traingle_area_perimeter(p1, p2, p3)
#                         if p - par_p < 0:
#                             continue
#                         ratio = (a - par_a) / (p - par_p)
#                         if ratio < choice[0]:
#                             choice = (ratio, a, p, p1, p2, p3, diff)
#                             flag = False
#
#             cur = cur.next
#         if flag:
#             break
#         else:
#             ratio, a, p, p1, p2, p3, diff = choice
#             area -= a
#             perimeter -= p
#             if diff is None:
#                 print(f"r={ratio} R={area / perimeter} p1={(p1.x, p1.y)} p2={(p2.x, p2.y)} p3={(p3.x, p3.y)}")
#                 p1.next = p3
#                 populate(p1, p3)
#                 print_points(head)
#             else:
#                 print(f"r={ratio} R={area / perimeter} p1={(p1.x, p1.y)} p2={(p2.x, p2.y)} p3={(p3.x, p3.y)}")
#                 p2.x -= diff[0]
#                 p2.y -= diff[1]
#                 populate(p1, p2)
#                 populate(p2, p3)
#                 print_points(head)
#
#     A = LIM * LIM * 4 - (LIM * LIM * 4 - area) * 4
#     P = LIM * 8 - (LIM * 8 - perimeter) * 4
#     print()
#     return A, P, A / P

def check_sq(x):
    return ceil(x) == floor(x)


def points_generate(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    points = []
    if x1 == x2:
        # print('here',x1,y1,x2,y2)
        for i in range(y1, y2 - 1, -1):
            points.append((x1, i))
        return points
    m = (y1 - y2) / (x1 - x2)
    c = y1 - m * x1
    for x in range(x1, x2 + 1):
        y = m * x + c
        if check_sq(y):
            points.append((x, int(y)))
    return points


def dist(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def area_perimerter(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3

    area = 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
    perimeter = dist(p1, p2) + dist(p2, p3) - dist(p1, p3)

    return area, perimeter


def dfs(p1, p2, p3, A, P, depth):
    print(p1,p2,p3,A/P,depth)


    ratio = A / P
    p2_p1_points = points_generate(p1, p2)[::-1]
    p2_p3_points = points_generate(p2, p3)
    print(p2_p1_points)
    print(p2_p3_points)
    if depth > 2:
        return
    i, j = 1, 1

    while i < len(p2_p1_points) and j < len(p2_p3_points):
        p2_1 = p2_p1_points[i]
        p2_2 = p2_p3_points[j]

        d1 = dist(p2_1, p2)
        d2 = dist(p2, p2_2)

        # print(p2_1, p2_2, d1, d2)
        if d1 == d2:
            a, p = area_perimerter(p2_1, p2, p2_2)
            a *= 1 << depth
            p *= 1 << depth
            r = (A - a) / (P - p)
            # print(a, p,r)
            if r > ratio:
                dfs(p1, p2_1, p2_2, A - a, P - p, depth + 1)
            i += 1
            j += 1
        elif d1 > d2:
            j += 1
        else:
            i += 1


def trial2(p1, p2, p3):
    A = LIM * LIM * 4
    P = LIM * 8
    dfs(p1, p2, p3, A, P, 2)
    # ratio = A / P
    # print(A, P)
    #
    # points_p1p2 = points_generate(p1, p2)[::-1]
    # # ans = [p1,p2]
    # for depth in range(2, 4):
    #     print(p1, p2, p3)
    #     points_p2p3 = points_generate(p2, p3)
    #     points_p2p3.pop(0)
    #     print(points_p1p2)
    #     print(points_p2p3)
    #     i = 0
    #     while True:
    #         last_point = points_p1p2.pop(0)
    #         if last_point == p2:
    #             break
    #         i += 1
    #
    #     i, j = 0, 0
    #     r_best = [ratio, (0, 0)]
    #     while i < len(points_p1p2) and j < len(points_p2p3):
    #         p2_1 = points_p1p2[i]
    #         p2_2 = points_p2p3[j]
    #         d1 = dist(p2_1, p2)
    #         d2 = dist(p2, p2_2)
    #         if d1 == d2:
    #             a, p = area_perimerter(p2_1, p2, p2_2)
    #             a *= 1 << depth
    #             p *= 1 << depth
    #             r = (A - a) / (P - p)
    #             if r > r_best[0]:
    #                 print(p2_1)
    #                 r_best = [r, p2_1, p2_2]
    #             i += 1
    #             j += 1
    #         elif d1 > d2:
    #             j += 1
    #         else:
    #             i += 1
    #     print(r_best)
    #     if r_best[0] > ratio:
    #         ratio = r_best[0]
    #         p2 = r_best[1]
    #         p3 = r_best[2]
    #         # ans.append(p3)
    #         continue
    #     break


def solve():
    # head = Point(0, LIM)
    # p2 = Point(LIM, LIM)
    # p3 = Point(LIM, 0)
    # populate(head, p2)
    # populate(p2, p3)
    p1 = (0, LIM)
    p2 = (LIM, LIM)
    p3 = (LIM, 0)
    temp = trial2(p1, p2, p3)
    # print(head)
    # # populate(cur, Point(LIM, 0))
    # # print_points(head)
    # print_points(head)
    # dfs(head, 0, 0, 0)
    # print(len(mem), mem)
    # print_points(head)
    # temp = trial(head)
    # print_points(head)
    # print()
    return temp


mem = {}

print('ans =', solve())
# p1 = Point(27, 29)
# p2 = Point(29, 27)
# p1.next=p2
# populate(p1,p2)
# print_points(p1)
# p3 = Point(30, 25)
# print(change(p1,p2,p3,(1,0)))
# print(traingle_area_perimeter(p1, p2, p3))
# print(traingle_area_perimeter(10, 5, 10, 5, 20, 5))
# print(form(1))
# print(same_side(p1, p2, p3, (1, 0)))
print(round(time.time() - st, 2), 's')


def out(x1, y1, x2, y2, r):
    m = (y1 - y2) / (x1 - x2)
    c1 = y1 - m * x1
    a = 1 + m * m
    b = 2 * m * c1
    c = c1 * c1 - r * r
    d = b * b - 4 * a * c
    print(d)
    return d

# out(131,250,207,207,sqrt(500*500/pi))

# p1 = (0,10)
# p2 = (10,10)
# print(points_generate(p1,p2))
# populate(p1,p2)
# print_points(p1)
# x1y
