from time import time
import math
start_time = time()

# excess cost = math.hypot(dx, dy) / v - dx / R
# here we assume that we can travel at speed R, so when we move dy we have cost - cost removed of dx from total
# differentiate excess cost with dx and let it be 0 to get minima we get
#  dx = dy * v / math.sqrt(R * R - v * v)


D = 10000
R = D // 2
sqrt_D = math.ceil(math.sqrt(D))
log_y = [0.0] + [math.log(y) for y in range(1, R + 1)]
dp = [float('inf')] * (R + 1)
dp[1] = 0.0

for y in range(2, R + 1):
    log_y_val = log_y[y]
    max_dy = min(y - 1, sqrt_D)
    for y0 in range(y - 1, y - 1 - max_dy, -1):
        dy = y - y0
        v = dy / (log_y_val - log_y[y0])
        dx_star = dy * v / math.sqrt(R * R - v * v)
        k = int(dx_star)
        for dx in (k, k + 1):
            excess_cost = math.hypot(dx, dy) / v - dx / R
            cand = dp[y0] + excess_cost
            if cand < dp[y]:
                dp[y] = cand
total_time = 2.0 * dp[R] + 2.0
print(f"T({D}) = {total_time:.9f} (in {time() - start_time:.3f}s)")