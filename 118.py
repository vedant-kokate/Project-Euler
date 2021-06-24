import time
import math
from itertools import permutations
st=time.time()
def part(start,prev):
    
    num=0
    count=0
    for i in range(start,len(perm)):
        num=num*10+perm[i]
        # print(perm,num,prev)
        if num<prev:
            continue
        if not prime(num):
            continue
        if i==len(perm)-1:
            return count+1
        count+=part(i+1,num)
    return count

def prime(n):
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False
    if n < 25:
        return True

    s = int(math.sqrt(n))
    for i in range(5,s+1,6):
        if (n % i == 0):
            return False
        if (n % (i + 2) == 0):
            return False  

    return True
        


dig=[1,2,3,4,5,6,7,8,9]
ans=0
for perm in list(permutations(dig)):
    ans+=part(0,0)
print(ans)
print(time.time()-st,'s')