import time
st=time.time()
for n in range(51,10**6):
    ways=[1]*n
    for i in range(50,n):
        ways[i]=ways[i-1]+sum(ways[:i-50])+1
    if ways[-1]>10**6:
        print(n-1,ways[-1])
        exit()

print(time.time()-st,'s')