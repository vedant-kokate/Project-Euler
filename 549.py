import time
from collections import defaultdict
from math import sqrt, log

st = time.time()
import euler


def precompile(primes):
    mem = {}
    for p in primes:
        count = 0
        count_array = []
        for i in range(1, int(log(LIM, p)) + 1):
            pi = p * i

            while pi % p == 0:
                pi //= p
                count += 1
            count_array.append(count)
            if count > int(log(LIM, p)):
                break
        # print(p,count_array,p*i)
        idx = 0
        i = 1
        while idx<len(count_array):
            while i<=count_array[idx]:
                mem[(p,i)] = (idx+1)*p
                i+=1
            idx+=1
        # while i<int(log(LIM, p)) + 1:
        #     mem[(p,i)] = (idx+1)*p
        #     i+=1
    return mem
        # print(p, count_array)
    # print(mem)

def solve():
    primes = euler.list_primes(LIM)
    print("PRIMES GENERATED",time.time()-st,'s')
    mem = precompile(primes)
    print("PRECOMPILE COMPLETED",time.time()-st,'s')
    # print(mem)
    ans = [0] * (LIM + 1)
    for i in primes:
        for j in range(i, LIM + 1, i):
            # pass
            num = j
            count = 0
            while num % i == 0:
                count += 1
                num //= i
            ans[j] = max(ans[j],mem[(i,count)])
            # factors[j][i] = int(log(j, i))
    # print(ans[10],ans[25])
    # print(ans)
    return sum(ans)
    # ans = 0
    # for i in range(1,)


# fact = [1,1]
# LIM = 100
# for i in range(2,1000):
#     fact.append(fact[-1]*2)

LIM = 10 ** 8
print('ans = ', solve())
# print(is_47_smooth(2491))
print(time.time() - st, 's')
