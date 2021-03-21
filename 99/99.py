import time
import math
st=time.time()
f=open("/home/vedant/program files/Github/vedantkokate07/Project-Euler/99/p099.txt", "r")
ans=-1
Max=-1
for i in range(1000):
    x,y=map(int,f.readline().split(','))
    eq=y*math.log(x)
    if eq>Max:
        Max=eq
        ans=i
print(ans)
print(time.time()-st,'s')
