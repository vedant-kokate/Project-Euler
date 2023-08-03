import time
from fractions import Fraction as f
st = time.time()
lim = 15
def solve():
    fact = list(range(2,lim+2))
    print(fact)
    ans = f(0,1)
    for i in range(1<<lim):
        # print(i)
        prob = f(1,1)
        ones = 0
        for j in range(lim):
            if (1<<j)&i:
                prob *= f(1,fact[j])
                ones +=1
            else:
                prob *= f(fact[j]-1, fact[j])
        if ones>lim//2:
            ans+=prob
    return ans.denominator//ans.numerator


print('ans =', solve())
print(time.time() - st, 's')
