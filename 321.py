import itertools
from math import sqrt, ceil, floor
# https://www.alpertron.com.ar/QUAD.HTM
import time

st = time.time()
lim = 40


#
# def swap(arr, x, y):
#     temp = arr[x]
#     arr[x] = arr[y]
#     arr[y] = temp
#
#
# def recur(s, blank, d):
#     st = "".join(s)
#     if st in mem:
#         return -1
#
#     print(d, st, blank)
#     if st == 'b' * lim + ' ' + 'r' * lim:
#         exit()
#     if blank - 1 >= 0 and s[blank - 1] == 'r':
#         # print('1')
#         swap(s, blank, blank - 1)
#         x = recur(s, blank - 1, d + 1)
#         swap(s, blank, blank - 1)
#     if blank - 2 >= 0 and s[blank - 1] == 'b' and s[blank - 2] == 'r':
#         # print('2')
#         swap(s, blank, blank - 2)
#         recur(s, blank - 2, d + 1)
#         swap(s, blank, blank - 2)
#     if blank + 1 < len(s) and s[blank + 1] == 'b':
#         # print('3')
#         swap(s, blank, blank + 1)
#         recur(s, blank + 1, d + 1)
#         swap(s, blank, blank + 1)
#     if blank + 2 < len(s) and s[blank + 1] == 'r' and s[blank + 2] == 'b':
#         # print('4')
#         swap(s, blank, blank + 2)
#         recur(s, blank + 2, d + 1)
#         swap(s, blank, blank + 2)
#     mem[st] = True

def is_traingle(n):
    x = sqrt(8 * n + 1)
    return ceil(x) == floor(x)


def form(x, y):
    x, y = 3 * x + 4 * y + 5, 2 * x + 3 * y + 3
    return x, y


def solver(x, y):
    ans = []
    while len(ans)-1 < lim // 2:
        ans.append(y)
        x, y = form(x, y)
    return ans

def solve():
    ans = sorted(solver(0,0) + solver(2,1))
    ans.pop(0)
    ans=ans[:lim]
    print(len(ans))
    return sum(ans)


# print('ans = ', recur(['r'] * lim + [' '] + ['b'] * lim, lim, 0))
print('ans =', solve())
print(time.time() - st, 's')
