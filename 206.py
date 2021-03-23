import time
st=time.time()
num=set()
for i in range(1000,10**4):
    n2=i*i
    n2=str(n2)
    if n2[-1]=='9' and n2[-3]=='8':num.add(i)


num2=[]
for i in range(100,1000):
    for j in num:
        n=str(i)+str(j)
        n=int(n)
        n2=n*n
        n2=str(n2)
        if n2[-5]=='7' and n2[-7]=='6':num2.append(n)


num3=[]
for i in range(10,100):
    for j in num2:
        n=str(i)+str(j)
        n=int(n)
        n2=n*n
        n2=str(n2)
        if n2[-9]=='5':num3.append(n)

for i in num3:
    s=str(i*i)
    if len(s)==17:
        if s[0]=='1' and s[2]=='2' and s[4]=='3' and s[6]=='4' and s[8]=='5':
            if s[10]=='6' and s[12]=='7' and s[14]=='8' and s[16]=='9':
                print(i*10,s)
                break
print(time.time()-st,'s')