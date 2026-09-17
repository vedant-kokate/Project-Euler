import numpy as np

def f(n):
    return sum((-1)**i * n**i for i in range(11))
def f2(n):
    return n**3

N = 10
sequence = [f(n) for n in range(1, N + 1)]
ans = 0

for k in range(1, N + 1):
    a = np.array([[n**power for power in range(k)] for n in range(1, k + 1)], dtype=np.float64)
    y = np.array(sequence[:k], dtype=np.float64)
    c = np.linalg.solve(a, y)
    fit = sum(c[power] * ((k+1)**power) for power in range(k))
    ans += round(fit)



print(ans)
