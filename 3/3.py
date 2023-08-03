import time

st = time.time()
lim = 600851475143
i = 2
while lim > 1:
    while lim % i == 0:
        lim //= i
        # print(lim,i)
    i += 1
print('ans =', i)
print(time.time() - st, 's')
