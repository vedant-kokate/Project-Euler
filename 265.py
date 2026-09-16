from time import time
start_time = time()
N = 5
mask = (1 << N) - 1
num_to_vis = 1 << N  # Fixed: 2^3 = 8 total patterns

def dfs(sequence, visited):
    if len(visited) == num_to_vis:
        return int(sequence[:-N + 1], 2)
        
    window = int(sequence[-N + 1:], 2) * 2
    zero = window
    one = zero + 1

    res = 0

    if one not in visited:
        res += dfs((sequence + "1"), visited | {one})

    if zero not in visited:
        res += dfs(sequence + "0", visited | {zero})
    return res

s = "0" * N
print(dfs(s, {0}))
print(f"Time taken: {time() - start_time:.2f}s")