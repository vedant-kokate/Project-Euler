from time import time
start = time()
N = 2 * 10**5
def solve(N=200000):
    # 1. Precompute complete tree coefficients (m, c) for length L
    m, c = [0] * (N + 1), [0] * (N + 1)
    G = [2**k - 1 for k in range(1, 20)]
    g_idx = 0
    
    for L in range(1, N + 1):
        if L == 1: m[1], c[1] = 1, 0; continue
        if L == 2: m[2], c[2] = 1, 1; continue
        while G[g_idx] < L: g_idx += 1
        t = G[g_idx - 1]
        d = min(t, L - (t - 1) // 2)
        m1, c1, m2, c2 = m[d - 1], c[d - 1], m[L - d - 1], c[L - d - 1]
        cr = c2 + m2 * (d + 1)
        m[L] = max(m1, m2) + 1
        c[L] = d + (c1 if m1 > m2 else (cr if m2 > m1 else max(c1, cr)))

    # 2. Compute C[n] DP
    C = [0, 0, 1, 2, 4, 6, 8] + [0] * (N - 6)
    dist, j_lim = 3, 2
    jumps = [0] + [1 << p for p in range(2, 18)]

    for n in range(7, N + 1):
        if dist > 4**j_lim: j_lim += 1
        best = float('inf')
        for delta in jumps[:j_lim]:
            k = n - dist - delta
            if k <= 0: continue
            r_L = n - k - 1
            right = m[r_L] * (k + 1) + c[r_L] if r_L > 0 else 0
            cost = k + max(C[k - 1], right)
            if cost < best:
                best, best_dist = cost, dist + delta
        C[n], dist = best, best_dist

    return sum(C)

print(solve(N))
print(f"Time taken: {time() - start:.2f}s")
