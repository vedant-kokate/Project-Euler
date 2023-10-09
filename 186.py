import time
from collections import defaultdict, deque

st = time.time()
mod = 10 ** 6


def combine_sets_with_no_common_elements(sets_list):
    combined_sets = []  # Initialize an empty list to store the combined sets

    for current_set in sets_list:
        # Check if the current set has common elements with any combined set
        has_common_elements = False
        for combined_set in combined_sets:
            if len(current_set.intersection(combined_set)) > 0:
                # Merge the current set with the combined set
                combined_set.update(current_set)
                has_common_elements = True
                break

        if not has_common_elements:
            # If no common elements were found, add the current set as a new combined set
            combined_sets.append(current_set)

    return combined_sets


def get_leader(d, num):
    while True:
        # print('getting leader',num)
        if d[num][0] == num:
            exit()
        if d[num][0] == -1:
            return num
        num = d[num][0]
    return num


def combine_num1_num2(num1, num2, d, children):
    global max_
    num1_in = num1 in d
    num2_in = num2 in d
    # print(num1, num2, num1_in, num2_in)

    if not num1_in and not num2_in:
        d[num1] = [-1, 1]
        d[num2] = [num1, 0]
        children[num1] = {num2}


    elif num1_in and not num2_in:
        l = get_leader(d, num1)
        d[l][1] += 1
        max_ = max(max_, d[l][1])
        d[num2] = [l, 0]
        children[l].add(num2)

    elif not num1_in and num2_in:
        l = get_leader(d, num2)
        d[l][1] += 1
        max_ = max(max_, d[l][1])
        d[num1] = [l, 0]
        children[l].add(num1)
    else:
        l1 = get_leader(d, num1)
        l2 = get_leader(d, num2)

        if l1 == l2:
            return False

        d_l1 = d[l1]
        d_l2 = d[l2]
        if d_l1[0] > d_l2[0]:
            d[l1][1] += d_l2[1]
            max_ = max(max_, d[l1][1])
            d[l2] = [l1, 0]
            for child in children[l2]:
                d[child][0] = l1
            del children[l2]
        else:
            d[l2][1] += d_l1[1]
            max_ = max(max_, d[l2][1])
            d[l1] = [l2, 0]
            for child in children[l1]:
                d[child][0] = l2
            del children[l1]
    return False


def genrate_fibo(lim):
    f = []
    d = {}

    for k in range(1, 56):
        num = 100003 - 200003 * k + 300007 * k * k * k
        num %= mod
        d[num] = True
        f.append(num)

    for k in range(56, lim + 1):
        # print('k', k,max_/mod)
        if len(d) == mod:
            return f
        num = (f[k - 25] + f[k - 56]) % mod
        if num == target:
            print(k, 'PM')
        d[num] = True
        f.append(num)
    return f


def bfs(f):
    g = {}
    for i in range(0, len(f)-1, 2):
        a, b = f[i], f[i + 1]
        if a == b:
            continue

        if a in g:
            g[a].add(b)
        else:
            g[a] = {b}
        if b in g:
            g[b].add(a)
        else:
            g[b] = {a}
    stack = deque([target])
    vis = {}
    vis[target] = True
    while stack:
        cur = stack.popleft()
        for neigh in g[cur]:
            if neigh not in vis:
                vis[neigh] = True
                stack.append(neigh)
    calls = 0
    for i in range(0, len(f) - 1, 2):
        if f[i] != f[i + 1]:
            calls += 1
    return len(vis), calls


def solve():
    lim = 4684406
    f = genrate_fibo(lim)
    print('f genrated')
    l = 4651260
    h = 4651276
    print(h-l)
    for m in range(l,h):
        connected, calls = bfs(f[:m])
        print(m, calls, connected / mod)
        if connected/mod==.99:
            return calls

    # print(connected*100/mod)
    # print("fibo done")
    # l=[]
    # for i in range(0,20000,2):
    #     if fibo[i]!=fibo[i+1]:
    #         l.append({fibo[i],fibo[i+1]})
    #
    # l=combine_sets_with_no_common_elements(l)
    # print(len(l))
    # print(len(g[524287]))
    # for i i


# genrate_fibo()
target = 524287
max_ = 0
print('ans=', solve())
print(time.time() - st, 's')
