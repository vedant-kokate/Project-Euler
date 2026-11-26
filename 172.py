import time
from functools import cache

st = time.time()
DIGIT_LIMIT = 18
COUNT_LIMIT = 3

@cache
def dp(pos, count):
    if pos == DIGIT_LIMIT: return 1
    total = 0
    for dig in range(10):
        if count[dig] < COUNT_LIMIT:
            new = list(count); new[dig] += 1
            total += dp(pos + 1, tuple(new))
    return total

total = 0
for dig in range(1, 10):
    count = [0] * 10; count[dig] = 1
    total += dp(1, tuple(count))
    
print(total)
print(time.time() - st, 's')


