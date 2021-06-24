from math import sqrt
from time import time
# @jit(target ="cuda")   
def solve():
    n=1
    arr=[]
    limit=10**14
    for n in range(1,limit):
        if n*(n+1)<=limit:
            arr.append(n*(n+1))
        else:
            break

    checker=set()
    ans=0
    for i,val in enumerate(arr):
        if val**2>limit:
            break
        st=0
        ed=len(arr)-1
        while ed-st>1:
            mid=(ed+st)//2
            value=arr[mid]*val
            if value>limit:
                ed=mid
            else:
                st=mid
        ans+=st-i
        for j in range(st,i-1,-1):
            checker.add(arr[j]*val)
    print(len(checker))
    print(ans)


if __name__=="__main__":
    start_time=time()
    solve()
    
    print(time()-start_time,'seconds')