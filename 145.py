import time
st=time.time()
def check(s):
    s=str(s)
    l={'0','2','4','6','8'}
    for ch in s:
        if ch in l:
            return False
    return True

ans= 0
lim = 10**7
vis={}
for i in range(10**6,lim):
    if i in vis or i%10==0:
        continue
    rev = int(str(i)[::-1])
    s= rev+i
    if check(s):
        ans+=2
        # print(i)
        vis[rev]=True
print(ans)

20 + 100 + 600 + 18000 +  5*10**4 + 54*10**4
print(time.time()-st,'s')