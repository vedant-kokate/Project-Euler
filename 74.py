import time
from collections import defaultdict
st=time.time()
n=10**6
# vis=defaultdict(bool)
ans=0
fact={'0':1,'1':1,'2':2,'3':6,'4':24,'5':120,'6':720,'7':5040,'8':40320,'9':362880}
def get_next(num):
    f=0
    for dig in str(num):
        f+=fact[dig]
    #print(f)
    return f

for i in range(1,n):
    chain=set()
    num=i
    while num not in chain:
        chain.add(num)
        num=get_next(num)
    if len(chain)==60:
        ans+=1

print(ans)
print(time.time()-st,'s')