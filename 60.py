import time
import math
from collections import defaultdict
st=time.time()
def comb(a, b):
    # print(a,b)
    if isPrime(int(str(a)+str(b))) and isPrime(int(str(b)+str(a))):
        return True
    return False

def isPrime(n) : 
	if (n <= 1) : 
		return False
	if (n <= 3) : 
		return True
	if (n % 2 == 0 or n % 3 == 0) : 
		return False
	i = 5
	while(i * i <= n) : 
		if (n % i == 0 or n % (i + 2) == 0) : 
			return False
		i = i + 6
	return True


n=10**4
p=[True]*n
for i in range(2,n):
    if p[i]:
        for j in range(i*2,n,i):
            p[j]=False
p2=[]
for i in range(2,n):
    if p[i]:
        p2.append(i)
print(len(p2))
m=len(p2)
def solve():
    for i in range(m):
        for j in range(i+1,m):
            if comb(p2[i],p2[j]):
                for k in range(j+1,m):
                    if comb(p2[i],p2[k]) and comb(p2[j],p2[k]):
                        for l in range(k+1,m):
                            if comb(p2[i],p2[l]) and comb(p2[j],p2[l]) and comb(p2[k],p2[l]):
                                for x in range(l+1,m):
                                    if comb(p2[i],p2[x]) and comb(p2[j],p2[x]) and comb(p2[k],p2[x]) and comb(p2[l],p2[x]):
                                        print(p2[i],p2[j],p2[k],p2[l],p2[x])
                                        print(p2[i]+p2[j]+p2[k]+p2[l]+p2[x])
                                        return
solve()



print(time.time()-st,'s')