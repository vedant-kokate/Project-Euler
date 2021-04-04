import time
st=time.time()
n=50
ways=[1]+[0]*50
for i in range(1,n+1):
    for j in range(1,5):
        if i-j>=0:
            ways[i]+=ways[i-j]
print(ways[-1])
print(time.time()-st,'s')