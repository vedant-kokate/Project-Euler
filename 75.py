import time
import math
from collections import defaultdict
st=time.time()
lim=int(1.5*10**6+1)
tri=[0]*(lim)
for m in range(int(math.sqrt(lim))):
    for n in range(1,m):
        if (m+n)%2==1 and math.gcd(m,n)==1:
            # print('here')
            a,b,c=m*m-n*n,m*m+n*n,2*m*n
            p=a+b+c
            k=1
            while p*k<lim:
                
                tri[p*k]+=1
                k+=1
        
print(tri.count(1))

            



print(time.time()-st,'s')