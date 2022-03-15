import time
st=time.time()

b,n = 15,21
lim = 10**12
while n <lim:
    b,n =  3 * b + 2 * n - 2,4 * b + 3 * n - 3

print(b)
print(time.time()-st,'s')

