import time
import euler

st = time.time()
target = 2000


def form(n):
    if n == 0:
        return 1
    return 3 * n * n - 3 * n + 2


def neigh1(n):
    return [6 * n + 1, 6 * n - 1, 12 * n + 5]


def neigh2(n):
    return [n * 6 - 7, 12 * n - 19, 6 * n - 1]


def solve():
    nums = [1, 2, 8]
    n = 3

    while len(nums) < target:
        num = form(n)
        if all(euler.is_prime(x) for x in neigh1(n)):
            nums.append(num)

        if all(euler.is_prime(x) for x in neigh2(n)):
            nums.append(num-1)
        n+=1

    return nums[-1]


# print(neigh2(4))
print('ans =', solve())
print(time.time() - st, 's')
