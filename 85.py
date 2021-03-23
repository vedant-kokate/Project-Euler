def rec(n,m):
    return n*(n+1)*m*(m+1)//4
lim=2*10**6
lim_srt=int(lim**.5)+1
dif=10**9
ans=0
for i in range(1,lim_srt):
    for j in range(1,lim_srt):
        if abs(lim-rec(i,j))<dif:
            dif=abs(lim-rec(i,j))
            ans=i*j
print(ans,dif)