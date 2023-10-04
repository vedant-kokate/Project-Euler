import euler
import time
from math import ceil, sqrt

st = time.time()
LIM = 10**6

def form(a,b):
    return a*b%(a+b)==0

def solve():
    triplets = euler.pytha_trip(LIM)
    ans = 0
    for key,val in triplets.items():
        if len(val)<2:
            continue
        for b1 in range(1,len(val)):
            for b2 in range(b1):
                if form(val[b1],val[b2]):
                    ans+=1
    return ans
    # print(triplets)

print('ans =', solve())
# print(get_var(2,3))
print(time.time() - st, 's')
