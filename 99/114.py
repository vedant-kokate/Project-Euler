import time
st=time.time()
n=51
ways=[1]*n
for i in range(3,n):
    ways[i]=ways[i-1]+sum(ways[:i-3])+1
print(ways)


print(time.time()-st,'s')