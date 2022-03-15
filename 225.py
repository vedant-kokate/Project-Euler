import time
st=time.time()


num = 29
count = 1
target = 124
while count!=target :
    t1,t2,t3 = 1,1,3
    while not(t1==t2==t3==1) and t3!=0:
        t1,t2,t3 = t2,t3,(t1+t2+t3)%num
        # print(t1,t2,t3)
    if t3!=0:
        count+=1
    # print(count,num)
    num+=2
    
print(num-2)
print(time.time()-st,'s')

