
from time import time
start_time=time()

N = 100
ans=[0]*(N+1)
probs=[0]*5
probs[0] = probs[4] = 1/36
probs[1] = probs[3] = 2/9
probs[2] = 0.5
last_mem=0
for _ in range(10**5):
    for i in range(1,N//2+1):
        newans = 1
        for j in range(5):
            newgap = i+j-2
            if (newgap<0): 
                newgap=-newgap
            if (newgap>N//2): 
                newgap=N-newgap
            newans += probs[j] * ans[newgap]            
        ans[i]=newans              

print(round(ans[N//2],6))
print(time()-start_time,'seconds')