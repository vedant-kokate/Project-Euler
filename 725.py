import time

st = time.time()
from collections import defaultdict
from fractions import Fraction as f

def dp(arr, target, sum_):
    if sum_ == target:
        return [arr]
    ans = []
    for i in range(arr[-1], 10):
        if sum_ + i > target:
            break
        ans += dp(arr + [i], target, sum_ + i)
    return ans


def solve():
    # d = {idx: [] for idx in range(1, 10)}
    second_half = int('1' * N) * fact[N - 1]
    second_half %= MOD
    print(second_half)
    # second_half %= MOD
    ans = 0
    for target in range(1, 10):
        for start in range(1, target + 1):
            # print(list(dp([start], target, start)))

            for ways in dp([start], target, start):
                rep = defaultdict(int)
                for dig in ways+[target]:
                    rep[dig] += 1
                if len(ways) + 1 > N:
                    # print(ways)
                    continue
                # print(ways + [target], target * 2 * second_half, rep.values())
                # rep[start]
                denom = 1
                for r in rep.values():
                    if r > 1:
                        denom *= fact[r]
                        # val *= pow(fact[r], -1, MOD)
                zero_count =  N - len(ways) - 1
                if zero_count > 1:
                    denom *= fact[zero_count]
                # print(f(target * 2,denom),ways+[target],zero_count)
                ans += f(target * 2,denom)
                # ans %=MOD
            # d[target] +=
    print(ans)
    ans *= fact[N-1]*int('1'*N)
    ans%=MOD
    return ans


N = 2020
MOD = 10 ** 16

fact = [1, 1]
for i in range(2, N):
    fact.append((fact[-1] * i))
print('ans = ', solve())
# print(is_47_smooth(2491))
print(time.time() - st, 's')



# print(mod_inverse(2,10)),
