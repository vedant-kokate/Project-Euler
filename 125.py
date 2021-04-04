import time
import math
st=time.time()
lim=10**8
check={}
ans=0
sqrt=int(math.sqrt(lim))
for i in range(1,sqrt):
    num=i*i
    for j in range(i+1,sqrt):
        num+=j*j
        if num>lim:break
        s=str(num)
        if s==s[::-1] and s not in check.keys():
            check[s]=1
            ans+=num

print(ans)
# print(check.keys())
print(time.time()-st,'s')