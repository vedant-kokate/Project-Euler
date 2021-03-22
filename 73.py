import time
st=time.time()
stack=[(1,3,1,2)]
ans=0
while stack:
    ln,ld,rn,rd=stack.pop()
    n=ln+rn
    d=ld+rd
    if d<=12000:
        ans+=1
        stack.append((ln,ld,n,d))
        stack.append((n,d,rn,rd))
print(ans)
print(time.time()-st,'s')