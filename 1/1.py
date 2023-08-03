import time
st = time.time()
lim = 1000
ans = 0
for i in range(lim):
    if i % 3 == 0 or i % 5 == 0:
        ans += i
print('ans =', ans)
print(time.time() - st, 's')
