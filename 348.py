import time

from math import sqrt,ceil,floor

st = time.time()

def find_count(num):
    count = 0
    for cube in range(1, int(pow(num, 1 / 3)) + 1):
        sqaure = num - cube * cube * cube
        if sqaure < 0:
            break
        sqaure = sqrt(sqaure)
        if floor(sqaure) == ceil(sqaure):
            count += 1
    return count

def solve():
    ans=[]
    target=4
    n=10**5
    for i in range(1,n):
        if i%10**3==0:
            print(i*100/n,'%')
        num1 = int(str(i)+str(i)[::-1])
        num2 = int(str(i)+str(i)[::-1][1:])
        if find_count(num1)==target:
            ans.append(num1)
        if find_count(num2)==target:
            ans.append(num2)
        if len(ans)==5:
            return sum(ans)


    return ans


print('ans =', solve())
print(time.time() - st, 's')
