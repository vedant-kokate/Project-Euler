import time
st=time.time()
n=100
dp=[0]*(n+1)
dp[0]=1
for i in range(1,100):
    for j in range(i,n+1):
        dp[j]+=dp[j-i]
#print(dp)
print(dp[n])