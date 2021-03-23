import time
st=time.time()
bouncy=0
for i in range(1,10**9):
    s=str(i)
    temp=''.join(sorted(s))
    if s!=temp and s!=temp[::-1]:
        bouncy+=1
    if bouncy/i==.99:
        print(i)
        break


print(time.time()-st,'s')