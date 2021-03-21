import time
st=time.time()
n=10**6
p=[True]*n
for i in range(3,n,2):
    if not p[i]:
        continue
    for j in range(i*2,n,i):
        p[j]=False 

prime=[]
for i in range(56004,n):
    if p[i]:
        prime.append(str(i))

prime_clean={}
for i in prime:
    for dig in '0123456789':
        if i.count(dig)>=3:
            prime_clean[i]=dig
            break
replace = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
def solve(num,dig):
    ans=-1
    count=0
    for i in range(10):
        new_num=num.replace(dig,replace[i])
        if len(new_num)<len(num):
            count+=1
            continue
        if new_num not in prime_clean.keys():
            count+=1
        else:
            if ans==-1:

                ans=new_num
                
        if count>2:
            break
    if count==2:
        return(ans)
        

for num,digit in prime_clean.items():
    x = solve(num,dig)
    if x is not None:
        print(x)
        break
        




print(time.time()-st,'s')

