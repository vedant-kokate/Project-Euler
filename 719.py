import time
import euler
from fractions import Fraction as f
import sys

sys.setrecursionlimit(10 ** 6)
st = time.time()
lim = 10 ** 6 + 1

# stack = [(square_str, n)]
# while stack:
#     # print(stack)
#     num_str, cur_val = stack.pop()
#     if num_str == "" and cur_val == 0:
#         return True
#     for i in range(1, len(num_str) + 1):
#         part = int(num_str[:i])
#         if cur_val - part >= 0:
#             remaining_str = num_str[i:]
#             stack.append((remaining_str, cur_val - part))
# return False

memo = {}


def is_special_number(n):
    square = n ** 2
    square_str = str(square)


    # Memoization dictionary to store previously computed results

    def check_split_parts(num_str, num_parts):
        if num_str == "":
            return num_parts == 0

        if (num_str, num_parts) in memo:
            return memo[(num_str, num_parts)]

        for i in range(1, len(num_str) + 1):
            part = int(num_str[:i])

            if num_parts - part >= 0:
                remaining_str = num_str[i:]
                if check_split_parts(remaining_str, num_parts - part):
                    memo[(num_str, num_parts)] = True
                    return True

        memo[(num_str, num_parts)] = False
        return False

    return check_split_parts(square_str, n)




def solve():
    # v = 10 ** 4
    ans = 0
    for i in range(1, lim, 9):
        # if i > v:
            # print(v // 10 ** 4, '%', time.time() - st, 's')
            # v += 10 ** 4
        if is_special_number(i):
            ans += (i * i)
        if is_special_number(i - 1):
            ans += ((i - 1) ** 2)
    return ans


print('ans =', solve()-1)
# is_special_number(9)
print(time.time() - st, 's')
