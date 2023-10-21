import time

st = time.time()


def A(k, n):
    last_f = 1
    ans = 0
    two_power = pow(2, n // k, MOD)
    for a in range(n // k + 1):
        if a % (10 ** 6) == 0:
            print(a / (n // k) * 100, '%')
        ans += (last_f * pow(two_power, k - 2 * a, MOD)) % MOD
        last_f *= ((k - 2 * a) * (k - 2 * a - 1)) % MOD
        last_f *= pow((a + 1) ** 2, -1, MOD)
        last_f %= MOD

    return ans%MOD


def solve():
    return A(K, N)


K, N = 10 ** 8, 10 ** 16
MOD = 10 ** 9 + 7
print('ans = ', solve())
# print(is_47_smooth(2491))
print(time.time() - st, 's')
