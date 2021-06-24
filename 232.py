
from time import time
from math import log 
start_time=time()
mem={}
target=100

def prob(n,m):
    global mem
    if m>=target:
        return 1
    if n>=target:
        return 0
    if n not in mem:
        mem[n]={}
    if m in mem[n]:
        return mem[n][m]
    
    max_prob=0
    t=1
    while True:
        n2=n+1
        m2=m+2**(t-1)
        P=(prob(n2, m2) + prob(n, m2)  + (2**t - 1) * prob(n2, m))/(2**t + 1) 
        max_prob=max(max_prob,P)
        t+=1
        if m2>=target:
            break
    mem[n][m]=max_prob
    return mem[n][m]    

ans=prob(0,0)/2+prob(1,0)/2
print(round(ans,8))
print(time()-start_time,'seconds')