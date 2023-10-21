import time
import euler

st = time.time()


def solve():
    prime = euler.list_primes(LIM)
    prime_sq = set()
    for p in prime:
        p2= p*p
        ps = str(p2)
        if ps!=ps[::-1]:
            prime_sq.add(ps)
    ans = []
    for ps in prime_sq:
        if ps[::-1] in prime_sq:
            ans.append(int(ps))
    ans.sort()
    print(len(ans))
    return sum(ans[:50])
LIM = 5*10**7
print('ans = ', solve())
# print(dist((290797, 629527), (3245540, 21669054)))
print(time.time() - st, 's')
