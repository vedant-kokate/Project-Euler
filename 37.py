count=0
num=11
n=10**6
ans=0
p=[True]*n
# s='123456'
# for i in range(len(s)):
#     print(s[i:],s[:len(s)-i])
for i in range(2,n):
    if not p[i]:
        continue
    for j in range(i*2,n,i):
        p[j]=False
prime={}
for i in range(2,n):
    if p[i]:
        prime[i]=1
#print(prime)
for num in prime.keys():
    if num<10:
        continue
    s=str(num)
    flag=True
    for i in range(len(s)):
        #print(int(s[i:]), int(s[i:]))
        if not(int(s[i:]) in prime.keys() and int(s[:len(s)-i]) in prime.keys()):
            flag=False
            break
            
    if flag:
        #print(num)
        ans+=num



print(ans)
        


