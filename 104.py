import time
import math
st=time.time()
mod = 10**9
def fastfib(n):

    bin_of_n = bin(n)[2:]  # binary string of n
    f = [0, 1]  # [F(i), F(i+1)] => i=0
 
    for b in bin_of_n:
        f2i1 = f[1]**2 + f[0]**2  # F(2i+1)
        f2i = f[0]*(2*f[1]-f[0])  # F(2i)
 
        if b == '0':
            f[0], f[1] = f2i, f2i1  # [F(2i), F(2i+1)]
        else:
            f[0], f[1] = f2i1, f2i1+f2i  # [F(2i+1), F(2i+2)]
 
    return f[0]
def second_check(n):
    s = str(fastfib(n))
    # s=
    if "".join(sorted(s[:9]))==check:
        # print(s)
        return True
    return False

check = "123456789"
a,b = 0,1

for i in range(10**6):
    if "".join(sorted(str(a))) == check:
        # print('first pass',i)
        if second_check(i):
            print(i)
            break
    a,b = b,(a+b)%mod
print(time.time()-st,'s')