import time
st=time.time()
lim = 100
def d_sum(n):
    s=0
    while n:
        r=n%10
        n//=10
        s+=r
    return s
# for a in range(2,lim):
#     c=(2*a+1)**2
# print(d_sum(123456789))
l=[]
for num in range(2,100):
    for power in range(1,100):
        x=pow(num,power)
        if x<10:
            continue
        if d_sum(x)==num:
            l.append(x)
l.sort()
print(l[1],l[9],l[29])
print(time.time()-st,'s')