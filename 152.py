import math
from time import time
from collections import Counter
start_time = time()
candidates = [2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 18, 20, 21, 24, 27, 28, 
              30, 32, 35, 36, 39, 40, 42, 45, 48, 52, 54, 56, 60, 63, 64, 65, 70, 72, 80]
#  , 70, 72, 80]
N = len(candidates)
squares = [c**2 for c in candidates]
total_lcm = math.lcm(*squares)
target = total_lcm // 2
terms = [total_lcm // sq for sq in squares]

mid = N // 2
left_terms = terms[:mid]
right_terms = terms[mid:]

right_counts = Counter()

def build_right(idx, current_sum):
    if idx == len(right_terms):
        right_counts[current_sum] += 1
        return
    build_right(idx + 1, current_sum + right_terms[idx])
    build_right(idx + 1, current_sum)

build_right(0, 0)

def dfs(cur_sum, idx):
    if idx == len(left_terms): return right_counts[target - cur_sum]
    if cur_sum > target or idx >= len(left_terms): return 0

    return dfs(cur_sum + left_terms[idx], idx + 1) + dfs(cur_sum, idx + 1)


ans = dfs(0, 0)
print(ans)
print("Time taken: {:.2f}s".format(time() - start_time))
