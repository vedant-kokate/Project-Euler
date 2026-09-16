import math

def is_non_terminating(a: int, b: int) -> bool:
    b_reduced = abs(b) // math.gcd(a, b)

    # 2. Strip ALL factors of 2 in O(1) time using bitwise masking
    b_reduced //= (b_reduced & -b_reduced)

    # 3. Strip all factors of 5
    while b_reduced % 5 == 0:
        b_reduced //= 5

    # If anything > 1 remains, it has prime factors other than 2 or 5
    return b_reduced > 1

def solve_fast(limit=100):
    total = 0
    k = 2
    # T_k is the exact boundary where N(n) transitions from k to k+1
    next_threshold = (k + 1) * ((1 + 1 / k) ** k)
    
    for n in range(5, limit + 1):
        while n >= next_threshold:
            k += 1
            next_threshold = (k + 1) * ((1 + 1 / k) ** k)
        
        # k is now N(n)
        if is_non_terminating(n, k):
            total += n
        else:
            total -= n
            
    return total

ans = solve_fast(10000)
print(f"Answer: {ans}")