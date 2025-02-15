import time

st = time.time()

def compute_winning_positions(limit):
    grundy = [0] * (limit + 1)
    losses = [1]
    for n in range(2, limit + 1):
        seen = set()
        for i in range(n - 1):
            j = (n - 2) - i
            if j >= 0:
                seen.add(grundy[i] ^ grundy[j])  # XOR for split positions 
            else:
                break
        val = min(x for x in range(len(seen) + 1) if x not in seen)
        if val == 0:
            losses.append(n)
        grundy[n] = val  # MEX function
        if len(losses) == 14:
            break
    while losses[-1]<limit:
        val = losses[-5] + 34
        losses.append(val)
    # print(losses, len(losses))
    return limit - len(losses) + 1

def solve():
    return compute_winning_positions(LIM)
LIM = int(input())
print('ans =', solve())
# print(f(9999))
print(round(time.time() - st, 2), 's')
