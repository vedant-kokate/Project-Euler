# import matplotlib.pyplot as plt
from collections import defaultdict
from operator import iand
from time import time
from itertools import combinations
start_time = time()

LIM = 500
lowest_points = {}
edges = defaultdict(list)
def orientation(p, q, r):
    """
    0  -> collinear
    1  -> counterclockwise
    -1 -> clockwise
    """
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])

    if val == 0:
        return 0

    return 1 if val > 0 else -1

def area(p, q, r):
    return abs((p[0] * (q[1] - r[1]) + q[0] * (r[1] - p[1]) + r[0] * (p[1] - q[1])) / 2.0)

def add_empty_triangle(a, b, c):
    if a not in lowest_points:
        lowest_points[a] = []
    lowest_points[a].append((b, c))
    edges[(a, b)].append(c)

blocked = defaultdict(bool)
def add_between_points(p, q, r):
    if min(p[0], q[0]) <= r[0] <= max(p[0], q[0]) and min(p[1], q[1]) <= r[1] <= max(p[1], q[1]):
        blocked[(p, q)] = True
        blocked[(q, p)] = True
    elif min(q[0], r[0]) <= p[0] <= max(q[0], r[0]) and min(q[1], r[1]) <= p[1] <= max(q[1], r[1]):
        blocked[(q, r)] = True
        blocked[(r, q)] = True
    else:
        blocked[(p, r)] = True
        blocked[(r, p)] = True




s = [290797]
points = []
t = []

while len(points) < LIM:
    s.append((s[-1] ** 2) % 50515093)
    t.append(s[-1] % 2000 - 1000)

    if len(t) % 2 == 0:
        points.append((t[-2], t[-1]))


print(f"Generated {len(points)} points in {time() - start_time:.2f} seconds")
# print(f"Points: {points}")
n = len(points)

left_points = defaultdict(int)

for i in range(n):
    p = points[i]
    for j in range(i + 1, n):
        q = points[j]
        for k in range(j + 1, n):
            r = points[k]
            o = orientation(p, q, r)
            if o > 0:
                left_points[(i, j)] |= 1 << k
                left_points[(j, k)] |= 1 << i
                left_points[(k, i)] |= 1 << j
            elif o < 0:
                left_points[(j, i)] |= 1 << k
                left_points[(k, j)] |= 1 << i
                left_points[(i, k)] |= 1 << j
            else:
                add_between_points(p, q, r)

print(f"Generated left points for {len(left_points)} edges in {time() - start_time:.2f} seconds")

for i in range(n):
    p = points[i]

    for j in range(i+1, n):
        q = points[j]

        for k in range(j+1, n):
            r = points[k]
            a, b, c = sorted([i, j, k],key=lambda x: (points[x][1], points[x][0]))
            o = orientation(points[a], points[b], points[c])
            if o > 0:
                if (left_points[(a, b)] & left_points[(b, c)] & left_points[(c, a)]) == 0:
                    add_empty_triangle(points[a], points[b], points[c])
            elif o < 0:
                if (left_points[(b, a)] & left_points[(c, b)] & left_points[(a, c)]) == 0:
                    add_empty_triangle(points[a], points[c], points[b])


        
print(f"Found {len(lowest_points)} empty triangles in {time() - start_time:.2f} seconds")

print(f"Generated {sum(len(v) for v in lowest_points.values())} empty triangles "
      f"across {len(lowest_points)} lowest points in {time() - start_time:.2f} seconds")
print(f"Generated {sum(len(v) for v in edges.values())} edges across {len(edges)} lowest points in {time() - start_time:.2f} seconds")

dp = defaultdict(float)

for a, bc_pairs in lowest_points.items():
    # sort by angle around a so the fan is processed in true topological order
    bc_pairs_sorted = sorted(bc_pairs, key=lambda bc: (bc[0][0], bc[0][1], bc[1][0], bc[1][1]))
    for b, c in bc_pairs_sorted:
        dp[(a, b, c)] = max(dp[(a, b, c)], area(a, b, c))
        if blocked[(a,c)]:
            continue
        for d in edges[(a, c)]:
            if orientation(b, c, d) >= 0:
                dp[(a, c, d)] = max(dp[(a, c, d)], area(a, c, d) + dp[(a, b, c)])

result = max(dp.values())
print(f"Maximum convex hole area: {result:.1f} (in {time() - start_time:.2f}s)")

