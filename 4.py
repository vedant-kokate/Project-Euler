import time

st = time.time()
m = 0
for i in range(100, 1000):
    for j in range(100, 1000):
        ans = str(i * j)
        if ans == ans[::-1] and int(ans) > m:
            m = int(ans)
print('ans =', m)
print(time.time() - st, 's')
