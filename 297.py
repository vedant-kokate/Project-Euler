from collections import deque
import time
from bisect import bisect_left as bl

st = time.time()
LIM = 10**17-1


def get_fibo_and_sum(n):
    f = [1, 2]
    fs = [1, 2]
    while f[-1] < n:
        cur = f[-1] + f[-2]
        f.append(cur)
        cur = fs[-1] + fs[-2] + f[-3] - 1
        fs.append(cur)
    return f, fs


def get_imp_val(val, f, fs):
    pos = bl(f, val)
    if f[pos] > val:
        pos -= 1

    red = val - f[pos]
    return red,fs[pos]

def solve():
    f, fs = get_fibo_and_sum(LIM)
    print(f)
    print(fs)
    ans = 0
    val = LIM
    while val:
        r,s = get_imp_val(val,f,fs)
        val = r
        ans += r+s
    return ans


print('ans =', solve())
# print(pow(10,2,7))
print(time.time() - st, 's')
