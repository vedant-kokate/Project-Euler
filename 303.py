import time

st = time.time()
LIM = 10
from collections import deque


def give_dig(n):
    if n == '0':
        return [str(x) for x in range(10)]
    elif n == '1':
        return ['0', '1', '2']
    elif n == '2':
        return ['0', '5', '6']
    elif n == '3':
        return ['4', '7']
    elif n == '4':
        return ['3', '5', '8']
    elif n == '5':
        return ['2', '4', '6', '8']
    elif n == '6':
        return ['2', '5', '7']
    elif n == '7':
        return ['3', '6']
    elif n == '8':
        return ['4', '5', '9']
    elif n == '9':
        return ['8', '9']


def check(n):
    # print(n)
    return not any(x not in ['0', '1', '2'] for x in n)

def compute_nine(n):
    print('here')
    for i in range(1,20):
        num = int('1'*i+'2'*4*i)
        # print(num)
        if num%n==0:
            return int(num)//n
def f(n):
    if all(x=='9' for x in str(n)):
        return compute_nine(n)
    stack = deque([(str(n), '')])
    ans =10**19
    while stack:
        # print(stack)
        num, x = stack.popleft()
        if check(num):
            if x == '':
                return 1
            else:
                ans = min(ans,int(x))
                continue
        if check(num[len(num) - 1 - len(x)]):
            stack.append((num, '0' + x))
        for dig in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            x2 = dig + x
            num2 = str(int(x2) * n)
            # print(x2,num2)
            if check(num2[len(num2) - 1 - len(x):]):
                if int(x2) >ans:
                    continue
                stack.append((num2, x2))

    return ans
def solve():
    ans = 0
    for i in range(1, 10001):
        x = f(i)
        ans += x
        print(i, x)
    return ans

print('ans =', solve())
# print(f(9999))
print(round(time.time() - st, 2), 's')
