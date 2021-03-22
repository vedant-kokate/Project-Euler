import time
from fractions import Fraction as f
st=time.time()
n=501
p=[True]*n
p[1]=False
mem={}
for i in range(1,n):
    if p[i]:
        mem[(i,'P')]=f(2,3)
        mem[(i,'N')]=f(1,3)
        for j in range(i*2,n,i):
            p[j]=False
    else:
        mem[(i,'P')]=f(1,3)
        mem[(i,'N')]=f(2,3)
ans=f(0,1)
def cal(i,s):
    if (i,s) in mem.keys():
        return mem[(i,s)]
    if i==1:    prob = mem[i,s[0]]*cal(i+1,s[1:])
    elif i==500:prob = mem[i,s[0]]*cal(i-1,s[1:])
    else:       prob = mem[i,s[0]]*(cal(i-1,s[1:])*f(1,2)+cal(i+1,s[1:])*f(1,2))
    mem[(i,s)] = prob
    return prob
s='PPPPNNPPPNPPNPN'
for i in range(1,n):
    ans+=cal(i,s)
print(ans/500)
print(time.time()-st,'s')