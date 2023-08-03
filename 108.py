import time
import itertools
import euler
st = time.time()
lim = 10**3

def count_divisors(n):
    count = 1
    end = euler.sqrt(n)
    for i in itertools.count(2):
        if i > end:
            break
        if n % i == 0:
            j = 0
            while True:
                n //= i
                j += 1
                if n % i != 0:
                    break
            count *= j * 2 + 1
            end = euler.sqrt(n)
    if n != 1:  # Remaining largest prime factor
        count *= 3
    return count

    return divisors



def solve():
    for i in itertools.count(1):
        if (count_divisors(i) + 1) // 2 > lim:
            return i

# print('ans =', solve())
print(count_divisors(6))
print(time.time() - st, 's')
