import time
st=time.time()
#r/s<p/q<a/b
r,s = 0,1
a,b = 3,7
q=10**6
lower_bound = 2
while q >= lower_bound:
    p = (a*q-1)//b
    if p*s > r*q:
        s = q
        r = p
        lower_bound = s//(a*s-b*r)
    q-=1
print(p,q)
print(time.time()-st,'s')