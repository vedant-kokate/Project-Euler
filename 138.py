import time
from math import sqrt,ceil,floor
from itertools import permutations
st=time.time()
# def check(a,b):
#     c=sqrt(a*a+b*b)
#     if ceil(c)==floor(c):
#         return True
#     return False
        
# ans=0
# save=[]
# for a in range(1,10**6):
#     b=2*a+1
#     if check(a,b):
#         save.append([a,b])  

#     b=2*a-1
#     if check(a,b):
#          save.append([a,b])


# print(save)
x=0
y=1
P = -9
Q = -4
K = -4
R = -20
S = -9
L = -8
ans=0
for i in range(12):
    x,y= P*x + Q*y + K,R*x + S*y + L
    a=abs(x)
    b1=2*a-1    
    c=sqrt(a*a+b1*b1)
    if ceil(c)==floor(c):
        ans+=c
    b2=a*2+1
    c=sqrt(a*a+b2*b2)
    if ceil(c)==floor(c):
        ans+=c
print(ans)


 
print(time.time()-st,'s')