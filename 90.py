import time
st=time.time()
from itertools import combinations
perm = list(combinations([0,1, 2, 3,4,5,6,7,8,9], 6) )
def cd(d,i):
    return d in perm[i]

def check(i,j):
    # for 01
    if not((cd(0,i) and cd(1,j)) or (cd(0,j) and cd(1,i))):        return False
    # for 04
    if not((cd(0,i) and cd(4,j)) or (cd(0,j) and cd(4,i))):        return False
    # for 09
    if not((cd(0,i) and (cd(9,j) or cd(6,j))) or (cd(0,j) and (cd(9,i) or cd(6,i)))):        return False
    # for 16
    if not((cd(1,i) and (cd(9,j) or cd(6,j))) or (cd(1,j) and (cd(9,i) or cd(6,i)))):        return False
    # for 25
    if not((cd(2,i) and cd(5,j)) or (cd(2,j) and cd(5,i))):        return False
    # for 36
    if not((cd(3,i) and (cd(9,j) or cd(6,j))) or (cd(3,j) and (cd(9,i) or cd(6,i)))):        return False
    # for 49
    if not((cd(4,i) and (cd(9,j) or cd(6,j))) or (cd(4,j) and (cd(9,i) or cd(6,i)))):        return False
    # for 64
    if not(((cd(9,i) or cd(6,i)) and cd(4,j)) or ((cd(9,j) or cd(6,j)) and cd(4,i))):        return False
    # for 81
    if not((cd(8,i) and cd(1,j)) or (cd(8,j) and cd(1,i))):        return False
    return True
   
print(len(perm))
ans=0
for i in range(210):
    for j in range(i):
        if check(i,j):
            ans+=1
print(ans)
print(time.time()-st,'s')