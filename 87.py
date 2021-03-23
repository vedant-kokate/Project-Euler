import time
st=time.time()
n=50000000+1
p=[True]*n
for i in range(2,n):
    if p[i]:
        for j in range(i*2,n,i):
            p[j]=False
sq=[]
cu=[]
fo=[]
for i in range(2,n):
    if p[i]:
        if i*i<n:
            sq.append(i*i)
            if i*i*i<n:
                cu.append(i*i*i)
                if i*i*i*i<n:
                    fo.append(i*i*i*i)

ans=set()
for i in sq:
    for j in cu:
        for k in fo:
            t=i+j+k
            if t<n:
                ans.add(t)
print(len(ans))
print(time.time()-st,'s')