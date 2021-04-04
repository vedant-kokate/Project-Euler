import time
import itertools
st=time.time()
n=10**3
p=[True]*n
c=[]
for i in range(2,n):
    if p[i]:
        c.append(i)
        for j in range(i*2,n,i):
            p[j]=False
# c=[2,3,5]
mod=10**9+7
dp=[0]*(n+1)
dp[0]=1
for i in c:
    for j in range(i,n+1):
        dp[j]+=dp[j-i]
        dp[j]%=mod
    if dp[i]>5000:
        print(i)
        break
   
#print(dp)
print(c[:10])
print(max(dp))
print(time.time()-st,'s')