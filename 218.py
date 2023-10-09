
import time
import math
st = time.time()
def generate_pythagorean_triplets(limit):
    res = 0
    for x in range(limit):
        for y in range(limit):
            a = (x*x-y*y)**2 -(2*x*y)**2
            b = 4*x*y*(x*x-y*y)
            if a<=0 or b<=0:
                continue
            print(a,b)
            if a*b%168!=0:
               res+=1
    return res





def solve():
    limit = 10**3
    res = generate_pythagorean_triplets(limit)
    return res


print('ans =', solve())
print(time.time() - st, 's')

# /usr/bin/python3 /Users/vedantkokate/Github/Project-Euler/test.py
# 2 7
# 3 17
# 4 31
# 6 71
# 7 97
# 8 127
# 10 199
# 11 241
# 13 337
# 15 449
# 17 577
# 18 647
# 21 881
# 22 967
# 24 1151
# 25 1249
# 28 1567
# 34 2311
# 36 2591
# 38 2887
# 39 3041
# 41 3361
# 42 3527
# 43 3697
# 45 4049
# 46 4231
# 49 4801
# 50 4999
# 52 5407
# 56 6271
# 59 6961
# 62 7687
# 63 7937
# 64 8191
# 69 9521
# 73 10657
# 76 11551
# 80 12799
# 81 13121
# 85 14449
# 87 15137
# 91 16561
# 92 16927
# 95 18049
# 98 19207
