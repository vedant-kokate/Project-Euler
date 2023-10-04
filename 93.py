import itertools
import time
from itertools import permutations
from math import ceil, floor


def recur(idx, arr, ans):
    global vis
    if len(arr) == idx:
        if ans > 0 and ceil(ans) == floor(ans):
            vis[ans] = True
        return
    last = arr[idx]
    recur(idx + 1, arr, last + ans)
    recur(idx + 1, arr, last * ans)
    recur(idx + 1, arr, ans - last)
    recur(idx + 1, arr, -ans + last)
    if ans != 0:
        recur(idx + 1, arr, last/ans)
    if last != 0:
        recur(idx + 1, arr, ans / last)


def ops(arrs):
    global vis
    vis = {}
    for arrx in permutations(arrs):
        arr = list(arrx)
        last = arr[0]
        recur(1, arr, last)
    for i in itertools.count(1):
        if i not in vis:
            return i - 1


def solve():
    ans = ""
    max_ = 0
    for a in range(7):
        for b in range(a + 1, 8):
            for c in range(b + 1, 9):
                for d in range(c + 1, 10):
                    x = ops([a, b, c, d])
                    if x > max_:
                        max_ = x
                        ans = f"{a}{b}{c}{d}"
                        # print(x, ans)
    return ans

vis = {}
st = time.time()
# print(ops([1,2,5,8]))
print('ans =', solve())
print(time.time() - st, 's')
