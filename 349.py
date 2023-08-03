import time

import euler

st = time.time()
lim = 10 ** 18


def solve():
    size = 100
    delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # Up, Right, Down, Left
    mat = [[0] * size for _ in range(size)]
    ant_pos = [size // 2 - 1, size // 2 - 1]
    count = 0
    ant_dir = 0
    mem = []
    mem_size = 5
    for _ in range(lim):
        curr_state = mat[ant_pos[0]][ant_pos[1]]
        ant_dir = (ant_dir + (1 if curr_state == 0 else -1)) % 4
        mat[ant_pos[0]][ant_pos[1]] = 1 - curr_state
        ant_pos = [ant_pos[0] + delta[ant_dir][0], ant_pos[1] + delta[ant_dir][1]]
        count += 1 if curr_state == 0 else -1
        if _ % 104 == lim % 104:
            mem.append(count)
            if len(mem)>mem_size:
                mem.pop(0)
            if len(mem)==mem_size:
                flag = True
                for x in range(2,mem_size):
                    if mem[x]-mem[x-1]!=mem[1]-mem[0]:
                        flag=False
                        break
                if flag:
                    print(mem,_)
                    return (lim - _)//104*(mem[-1]-mem[-2])+count



    return count


print('ans =', solve())
print(time.time() - st, 's')
