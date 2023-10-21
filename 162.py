import time

st = time.time()
LIM = 2560000

def form(n):
    return 15 * pow(16,n-1) - 43 * pow(15,n-1) + 41 * pow(14,n-1) -pow(13,n)

def solve():
    ans = sum(form(n) for n in range(1,17))
    return f"{ans:X}"

print('ans =', solve())

print(time.time() - st, 's')
