import time
import euler
from fractions import Fraction as f

st = time.time()
lim = 10 ** 5 + 1


def ncr(n,r):
    ans = f(1,1)
    for k in range(1,r+1):
        ans /= k
        ans*=n
        n-=1
    return ans

def solve():
    ans = ncr(60,40)/ncr(70,20)
    ans = 1-ans
    ans *=7
    return f"{ans.numerator / ans.denominator:.9f}"


print('ans =', solve())
print(time.time() - st, 's')
