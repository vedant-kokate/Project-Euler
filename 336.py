import time

import euler

st = time.time()
target = 2011
num_of_alpha = 11


def next_permutation(s):
    arr = list(s)
    i = len(arr) - 2

    # Find the first element from the end that is less than its adjacent element
    while i >= 0 and arr[i] >= arr[i + 1]:
        i -= 1

    if i >= 0:
        j = len(arr) - 1

        # Find the smallest element greater than the element at index i
        while arr[j] <= arr[i]:
            j -= 1

        arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1:] = reversed(arr[i + 1:])

    # Convert the list of characters back to a string
    return ''.join(arr)


def recur(cur_tar, s):
    i = ord(cur_tar) - 65
    # print(i,cur_tar,s)

    if s[i] == cur_tar:
        return 0
    if i<len(s)-2 and s[-1]==cur_tar:
        return 0
    if i == len(s) - 2:
        return 1
    while i < len(s) - 1:
        i += 1
        if s[i] == cur_tar:
            s = s[:i] + s[i:][::-1]
            i = ord(cur_tar) - 65
            s = s[:i] + s[i:][::-1]
            break
    ans = recur(chr(i + 65 + 1), s)

    return ans


def solve():
    s = ''.join(['C', 'A', 'B'] + [chr(i + 68) for i in range(num_of_alpha - 3)])
    # s='ABCD'
    count = 0
    while True:
        # print(s)
        if recur('A', s):
            count += 1
            # print(count, s)
            if count == target:
                return s
        s = next_permutation(s)


mem = {}
# print(recur('A','DACB'))
print('ans =', solve())
print(time.time() - st, 's')
