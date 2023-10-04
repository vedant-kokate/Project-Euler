import euler
import math
import time

st = time.time()
lim = 10 ** 6 +1


def solve():
    ans = 0
    for b in range(10):
        for c in range(10):
            for d in range(10):
                for e in range(10):
                    for i in range(10):
                        m = b + c + d - e - i
                        if m < 0 or m > 9: continue
                        for k in range(10):
                            f = b + c + d * 2 - e - i - k
                            if f < 0 or f > 9: continue
                            for a in range(10):
                                for g in range(10):
                                    o = a + b + d - g - k
                                    if o < 0 or o > 9: continue
                                    j = a + b + c - g - m
                                    if j < 0 or j > 9: continue
                                    l = a + b + c + d - i - j - k
                                    if l < 0 or l > 9: continue
                                    h = a + b + c + d - e - f - g
                                    if h < 0 or h > 9: continue
                                    n = a + c + d - f - j
                                    if n < 0 or n > 9: continue
                                    p = a + b + c - h - l
                                    if p < 0 or p > 9: continue
                                    ans += 1
    return ans

print('ans =', solve())
print(time.time() - st, 's')
