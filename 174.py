import time
import math
st=time.time()
n=10**6
ans=[0]*(n+1)
for i in range(3,n//4+2,2):
    for j in range(i-2,0,-2):
        if i*i-j*j>n:
            break
        ans[i*i-j*j]+=1
for i in range(4,n//4+2,2):
    for j in range(i-2,1,-2):
        if i*i-j*j>n:
            break
        ans[i*i-j*j]+=1
res = 0
for i in range(1,11):
    x = ans.count(i)
    # print(i,x)
    res+=x
print('ans=',res)
print(time.time()-st,'s')