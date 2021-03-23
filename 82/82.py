import time
st=time.time()
f=open('/home/vedant/program files/Github/vedantkokate07/Project-Euler/82/p082.txt','r')
from collections import deque
n=80
mat=[]
for i in range(n):
    s=f.readline()
    # print(s)
    temp=s.split(',')
    if temp[-1][-1:]=='\n':
        temp[-1]=temp[-1][:-1]
    temp=list(map(int,temp))
    mat+=[temp]

stack=deque()
d=[[10**7 for i in range(n)]for j in range(n)]
for i in range(n):d[i][0]=mat[i][0]
r=[1,-1,0,0]
c=[0,0,1,-1]
for i in range(n):
    d[i][0]=mat[i][0]
    stack.append((i,0,d[i][0]))
    while stack:
        # print(stack)
        x,y,dist=stack.popleft()
        for i in range(4):
            xi=x+r[i]
            yi=y+c[i]
            # print(0<=xi<n,0<=yi<n,dist+mat[xi][yi]<d[xi][yi])
            if 0<=xi<n and 0<=yi<n and dist+mat[xi][yi]<d[xi][yi]:
                # print("here.................")
                d[xi][yi]=dist+mat[xi][yi]
                stack.append((xi,yi,d[xi][yi]))
ans=10**7
for i in range(n):
    ans=min(ans,d[i][-1])
print(ans)
# for i in d:
#     print(i)



print(time.time()-st,'s')