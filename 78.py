import time
import itertools
st=time.time()
p=[1]
mod=10**6
for i in itertools.count(1):
    x=0
    for j in itertools.count(1):
        sign=-1 if j%2==0 else 1         
        i1=j*(3*j-1)//2
        if i1>i:
            break
        x+=p[i-i1]*sign
        i2=j*(3*j+1)//2
        if i2>i:
            break
        x+=p[i-i2]*sign
        x%=mod
    p.append(x)
    if x==0:
        print(i)
        break

print(time.time()-st,'s')