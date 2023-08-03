import euler
import time

st = time.time()
lim = 5 * 10 ** 7 + 1


def f(n):
    return 2 * n * n - 1


def solve():
    check = [(2 * n * n - 1) for n in range(lim)]
    ans = 0
    for i in range(2, lim):
        num = check[i]
        if num == 1:
            continue
        # print(i,num)
        ans += num == 2 * i * i - 1
        for j in range(1, lim):
            val1 = i + num * j

            if val1 < lim:
                num1 = check[val1]
                while num1 % num == 0:
                    num1 //= num
                check[val1] = num1

            val2 = - i + num * j

            if val2 < lim:
                num2 = check[val2]
                while num2 % num == 0:
                    num2 //= num
                check[val2] = num2
            else:
                break
    return ans


print('ans =', solve())
print(time.time() - st, 's')

# /usr/bin/python3 /Users/vedantkokate/Github/Project-Euler/test.py
# 2 7
# 3 17
# 4 31
# 6 71
# 7 97
# 8 127
# 10 199
# 11 241
# 13 337
# 15 449
# 17 577
# 18 647
# 21 881
# 22 967
# 24 1151
# 25 1249
# 28 1567
# 34 2311
# 36 2591
# 38 2887
# 39 3041
# 41 3361
# 42 3527
# 43 3697
# 45 4049
# 46 4231
# 49 4801
# 50 4999
# 52 5407
# 56 6271
# 59 6961
# 62 7687
# 63 7937
# 64 8191
# 69 9521
# 73 10657
# 76 11551
# 80 12799
# 81 13121
# 85 14449
# 87 15137
# 91 16561
# 92 16927
# 95 18049
# 98 19207
