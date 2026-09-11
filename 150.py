import itertools
import math

import euler
import time

st = time.time()
LIM = 500501


def triangle_generator():
    t = 0
    s = []
    for k in range(1,500501):
        t = (615949*t + 797807) % 2**20
        s.append(t - 2**19)
        #First I generate the s values
    triangle = []
    r = 1000
    while r != 0:
        row = []
        for x in range(r):
            temp = s.pop(-1)
            row.insert(0,temp)
        triangle.insert(0, row)
        r -= 1
    #Now I make it into a triangle, mabye not the most efficient method
    return triangle

       

def solve():
    triangle = triangle_generator()
    sum_triangle = [row.copy() for row in triangle]

    for i in range(len(sum_triangle)):
        for j in range(1, len(sum_triangle[i])):
            sum_triangle[i][j] += sum_triangle[i][j-1]

    ans = 10**10

    for i in range(len(triangle)):
        for j in range(len(triangle[i])):
            current_sum = triangle[i][j]
            ans = min(ans, current_sum)

            for k in range(1, len(triangle)-i):
                current_sum += sum_triangle[i+k][j+k]

                if j-1 >= 0:
                    current_sum -= sum_triangle[i+k][j-1]

                ans = min(ans, current_sum)
        if i % 100 == 0:
            print(i, ans, round(time.time() - st, 2), 's')
    
    return ans

print('ans =', solve())
# print(pow(10,2,7))
print(time.time() - st, 's')
