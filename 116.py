import time
st=time.time()
def f(n,m):
    # print(n,m)
    if n<m: return 0
    if n in mem.keys():
        return mem[n]
    ans=0
    for i in range(n-m+1):
        ans+=1
        ans+=f(n-m-i,m)
    mem[n]=ans
    return ans
mem={}
Ans=0
for c in range(2,5):
    mem={}
    Ans+=f(50,c)
print(Ans)
print(time.time()-st,'s')