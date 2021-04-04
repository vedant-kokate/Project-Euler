import time
st=time.time()
ans=0
for i in range(3,1001):
    if i%2:
        r=i*(i-1)
    else:
        r=i*(i-2)
    ans+=r
print(ans)
print(time.time()-st,'s')