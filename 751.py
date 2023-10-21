import time
from collections import defaultdict

st = time.time()


def generate(theta, n):
    b1 = theta
    a = []
    while len(a) < n:
        a.append(str(int(b1)))
        b1 = int(b1) * (b1 + 1 - int(b1))
    s = a[0] + '.' + ''.join(a[1:])

    return s[:DIGIT_LIM + 2]


def solve():
    theta = 2.0
    step = 0.1
    vis = defaultdict(int)
    while True:
        s = generate(theta, DIGIT_LIM + 2)
        vis[theta] += 1
        if vis[theta]>=10:
            return s
        # print(s, theta)
        if s == str(theta):
            return s
        if float(s) - theta > 0:
            theta += step
        else:
            theta -= step
            step /= 10
            theta += step
    # print(generate(theta, 20))


DIGIT_LIM = 24
print('ans = ', solve())
# print(is_47_smooth(2491))
print(time.time() - st, 's')
