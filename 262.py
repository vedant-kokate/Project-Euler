import math
from time import time
start_time = time()
start_x, start_y = 200, 200
end_x, end_y = 1400, 1400
def height(x,y):
    return ( 5000-0.005*(x*x+y*y+x*y)+12.5*(x+y) ) * math.exp( -abs(0.000001*(x*x+y*y)-0.0015*(x+y)+0.7) )

def move(m,x,y,d):
    new_X = d/math.sqrt(1+m*m)
    new_Y = m*new_X
    return (x+new_X, y+new_Y)

def tangent(x, y, m, d, max_h):
    # pattern is to reach contour hign and go down before reaching boundry
    while True:
        x, y = move(m, x, y, d)
        h = height(x,y)
        if h > max_h:
            return -1
        if not (0 <= x <= 2000 and 0 <= y <= 2000):
            return 1

def find_tangent_slope(x, y, cur_slope, slop_incr, max_h):
    for i in range(10**2):
        t = tangent(x, y, cur_slope + slop_incr, -0.1, max_h)
        if t == 1:
            cur_slope += slop_incr
        elif t == -1:
            slop_incr /= 2
    return cur_slope 

def find_point_on_contour(x, y, m, max_h):
    alpha = 10
    cur_h = height(x, y)
    for i in range(10**2):
        new_x, new_y = move(m, x, y, -alpha)
        new_h = height(new_x, new_y)
        if abs(new_h - max_h) < abs(cur_h - max_h):
            x, y = new_x, new_y
            cur_h = new_h
        else:
            alpha /= 2
    return (x,y)

alpha = 1
max_h = 0
x= 0
for i in range(10**6):
    cur_h = height(x,0)
    next_h = height(x+alpha,0)
    if next_h > cur_h:
        max_h = next_h
        x += alpha
    else:
        alpha /= 2
print(f"Max height at x={x} y=0: {max_h} (in {time() - start_time:.2f}s)")
# max_h = 10396.462189127302

m_a = find_tangent_slope(start_x, start_y, -1, -0.1, max_h)
print(f"Slope for point A: {m_a} (in {time() - start_time:.2f}s)")
# slop = -2.79841802111891

alpha = 10

a_x, a_y = find_point_on_contour(start_x, start_y, m_a, max_h)
print(f"Point on contour: x={a_x} y={a_y} h={max_h} (in {time() - start_time:.2f}s)")
    

m_b = find_tangent_slope(end_x, end_y, -1, 0.1, max_h)
print(f"Slope for point B: {m_b} (in {time() - start_time:.2f}s)")

b_x, b_y = find_point_on_contour(end_x, end_y, m_b, max_h)
print(f"Point on contour: x={b_x} y={b_y} h={max_h} (in {time() - start_time:.2f}s)")

def slope(x, y):
    e = 1e-5
    hx = (height(x+e,y) - height(x-e,y))/(2*e)
    hy = (height(x,y+e) - height(x,y-e))/(2*e)
    return -hx/hy

def traverse(x, y, bx, by, max_h, step=0.0005):
    dist = 0

    while math.dist((x,y),(bx,by)) > step:
        old = (x,y)

        m = slope(x,y)

        p1 = move(m,x,y, step)
        p2 = move(m,x,y,-step)

        # choose whichever tangent direction gets closer to B
        x,y = p1 if math.dist(p1,(bx,by)) < math.dist(p2,(bx,by)) else p2

        # pull back onto contour
        for _ in range(5):
            h = height(x,y)
            e = 1e-5
            hx = (height(x+e,y)-height(x-e,y))/(2*e)
            hy = (height(x,y+e)-height(x,y-e))/(2*e)

            x -= (h-max_h)*hx/(hx*hx+hy*hy)
            y -= (h-max_h)*hy/(hx*hx+hy*hy)

        dist += math.dist(old,(x,y))
        # print(f"x={x} y={y}")

    return dist

arc = traverse(a_x, a_y, b_x, b_y, max_h)

total = round(
    math.dist((start_x,start_y),(a_x,a_y))
    + arc
    + math.dist((end_x,end_y),(b_x,b_y))
, 4)

print(f"Total distance: {total} (in {time() - start_time:.2f}s)")



