LIMIT = 70
ROUND_LIMIT = 7
ARC_ANGLE = 72
from math import sin, cos, radians
from functools import lru_cache
from time import time
start_time = time()
@lru_cache(maxsize=None)
def traverse(point, count, angle):
    if count == 0 and point == (0,0):
        return 1
    if count == 0: return 0
    x,y = point
    count -= 1
    total = 0
    for new_angle in (ARC_ANGLE, -ARC_ANGLE):
        new_dir_ang, mov_dir_ang = (angle + new_angle) % 360, (angle + new_angle / 2.0) % 360
        x1, y1 = round(x + cos(radians(mov_dir_ang)), ROUND_LIMIT), round(y + sin(radians(mov_dir_ang)), ROUND_LIMIT)
        total += traverse((x1,y1), count, new_dir_ang)
    
    return  total

print(traverse((0,0), LIMIT, 0))
print(f"IN {round(time()-start_time, 2)} seconds")