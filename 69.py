n=10**6+1
ans=[i for i in range(n)]
prime=[True]*n
Prime=[]
for i in range(2,n):
    if not prime[i]:
        continue
    else:
        Prime.append(i)
    for j in range(i*2,n,i):
        prime[j]=False

#print(Prime[:10])
for primenum in Prime:
    for i in range(primenum,n,primenum):
        ans[i]=(ans[i]*(primenum-1))//primenum
Ans=0
Max=-1
for i in range(2,n-1):
    ans[i]=i/ans[i]
    if ans[i]>Max:
        Max=ans[i]
        Ans=i
print(ans[:10])
print(ans[-10:]) 
print(Ans,Max)