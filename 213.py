import euler
import time
from fractions import Fraction as f

st = time.time()
n = 30
N = 50


def poss(i, j):
    lim = [0, n - 1]
    if i in lim and j in lim:
        return 2
    if i in lim or j in lim:
        return 3
    return 4


def drop_flea(x, y, ans):
    temp = [[f(0, 1)] * n for i in range(n)]
    temp[x][y] = 1
    for _ in range(N):
        temp2 = [[f(0, 1)] * n for i in range(n)]
        for i in range(n):
            for j in range(n):
                if temp[i][j] != 0:
                    ways = poss(i, j)
                    p = temp[i][j] / ways
                    for r, c in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                        X, Y = i + r, j + c
                        if 0 <= X < n and 0 <= Y < n:
                            temp2[X][Y] += p
        temp = temp2.copy()
    for i in range(n):
        for j in range(n):
            ans[i][j] *= 1 - temp[i][j]
            ans[i][j] *= 1 - temp[n-1-i][j]
            ans[i][j] *= 1 - temp[i][n-1-j]
            ans[i][j] *= 1 - temp[n-1-i][n-1-j]



def solve():
    ans = [[f(1, 1)] * n for i in range(n)]
    for i in range(n // 2):
        for j in range(n // 2):
            # print(i, j)
            drop_flea(i, j, ans)
    return round(sum(sum(i) for i in ans),6)


print('ans =', solve())
print(time.time() - st, 's')
