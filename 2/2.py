import time

st = time.time()
lim = 4000000
a = 1
b = 2
ans = 0
while a <= lim:
    if a % 2 == 0:
        ans += a
    a, b = b, a + b
print('ans = ', ans)
print(time.time() - st, 's')
