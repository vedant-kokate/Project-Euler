import time
from collections import defaultdict
st=time.time()
n=1000
ans=0
p=defaultdict(int)
for a in range(1,n):
    for b in range(1,a):
        c=(a*a+b*b)**(0.5)
        if int(c)==c:
            p[a+b+c]+=1
            ans+=1
ans_key,ans_val=0,0
for key,val in p.items():
    if key>1000:
        continue
    #print(key,val)
    if val>ans_val:
        ans_val=val
        ans_key=key
print(ans_key,ans_val)
print(time.time()-st,'s')

