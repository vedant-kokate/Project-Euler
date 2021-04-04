import time
import math
st=time.time()
n=10**6
ans=0
for i in range(1,n//4+2):
    for j in range(i-2,0,-2):
        if i*i-j*j<=n :
            # print(i,j)
            ans+=1
        else:
            break
print(ans)
print(time.time()-st,'s')