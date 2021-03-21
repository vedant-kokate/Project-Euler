from collections import defaultdict
import time
st=time.time()
d=defaultdict(list)
n=10**4
for i in range(1,n):
    s=str(i*i*i)
    temp="".join(sorted(s))
    d[temp].append(s)
for key,value in d.items():
    if len(value)==5:
        print(value)
        break
print(time.time()-st,'s')