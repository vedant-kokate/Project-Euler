import time

st = time.time()
a = 0
b = 0
for i in range(101):
    a += i * i
    b += i
print('ans =', b * b - a)
print(time.time() - st, 's')
