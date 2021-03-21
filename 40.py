import time
st=time.time()
s=''
i=1
while len(s)<=10**6:
    s+=str(i)
    i+=1
ans=int(s[0])
for i in range(1,7):
    ans*=int(s[int('9'*i)])
print(ans)
print(time.time()-st,'s')