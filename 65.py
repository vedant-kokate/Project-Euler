import math
import time
from fractions import Fraction as frac
st=time.time()

rep=[1]
for i in range(1,35):
    rep.append(2*i)
    rep.append(1)
    rep.append(1)
rep=rep[:99]
rep=rep[::-1]
ans=frac(1,rep[0])
for i in range(1,len(rep)):
    ans+=frac(rep[i])
    ans=1/ans
ans+=2
print(ans)
ans=str(ans.numerator)
print(ans)
Ans=0
for i in ans:
    Ans+=int(i)
print(Ans)
