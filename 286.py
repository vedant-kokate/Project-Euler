import time
st=time.time()
def f(t,x,q):
    return 1-x/q if t else x/q

def prob(target,n,s,q):
    if n==target:
        if s==0:
            return 1
        return 0
    if s<0:
        return 0
    
    global dp

    if (n+1,s) in dp:
        p1 = dp[(n+1,s)]
    else:
        p1 = prob(target,n+1,s,q)*f(False,n+1,q)
        dp[(n+1,s)] = p1
    if (n+1,s-1) in dp:
        p2 = dp[(n+1,s-1)]
    else:
        p2 = prob(target,n+1,s-1,q)*f(True,n+1,q) 
        # dp[(n+1,s-1)] = p2
 
    return p1+p2


# x=prob(50,0,20,53)
# print(x<=2/100,x)

LL, LH = 50, 54
# while True:
#     print(LL)
#     if prob(50, 0, 20, LL)<=2/100:
#         LH = LL*2
#         break
#     LL*=2
# print(LL,LH)


for i in range(100):
    dp={}
    mid = round((LH+LL)/2,12)
    
    val = prob(50, 0, 20, mid)
    
    if val<2/100:
        LH = mid
    else:
        LL = mid
    print(mid,val,LL,LH)
print(round(LL,10),round(LH,2))
print(time.time()-st,'s')