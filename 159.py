from time import time
start_time = time()
N = 10**6
a = [0] * (N)

for i in range(2, N):
    a[i] = (i-1) % 9 + 1
    
for i in range(2, N ):
    for j in range(i*2, N, i):
        div = j // i
        
        a[j] = max(a[i] + a[div], a[j])
print(sum(a))
print("Time taken: {} seconds".format(time() - start_time))