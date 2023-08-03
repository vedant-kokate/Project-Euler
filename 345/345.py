import time

import euler
import time

st = time.time()
mat = []
f = open("/Users/vedantkokate/Github/Project-Euler/345/input.txt", "r")
for line in f:
    mat.append(list(map(int, line.split())))
n, m = len(mat), len(mat[0])


def solve():
    def dfs(row, vis, sum, atleast):
        if row == n:
            return sum

        if sum + maxRemainig[row] < atleast:
            return 0

        for col in range(n):
            if col in vis:
                continue
            cur = dfs(row + 1, vis | {col}, sum + mat[row][col], atleast)
            atleast = max(atleast, cur)
        return atleast

    arr = [max(row) for row in mat]
    maxRemainig = [sum(arr[:i+1][::-1]) for i in range(len(arr))][::-1]

    return dfs(0, set(), 0, 0)


print('ans =', solve())
print(time.time() - st, 's')
