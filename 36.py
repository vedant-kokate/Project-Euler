
n=10**6
ans=0
for i in range(n):
    if str(i)==str(i)[::-1] and bin(i)[2:]==(bin(i)[2:])[::-1]:
        ans+=i
print(ans)