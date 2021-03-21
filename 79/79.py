def top(v,vis,stack,dep):
    # print(stack,'stack')
    # print(vis,'vis')
    # print(v,'v',dep)
    vis[str(v)]=True
    
    for i in g[v]:
        
        if i not in vis.keys():
            top(i,vis,stack,dep+1)
    stack.append(v)


f=open("/home/vedant/program files/Project-Euler/79/text.txt", "r")
inp=[]
for i in range(50):
    inp.append(f.readline())
g={}
for i in inp:
    if i[0] in g.keys():
        g[i[0]].add(i[1])
    else:
        g[i[0]]=set()
        g[i[0]].add(i[1])
    if i[1] in g.keys():
        g[i[1]].add(i[2])
    else:
        g[i[1]]=set()
        g[i[1]].add(i[2])
for i in inp:
    for j in i:
        if j not in g.keys() and j!='\n':
            g[j]=set()
stack=[]
vis={}
#print(g)
for i in g.keys():
    if i not in vis:
        top(i,vis,stack,0)
#print(*stack[::-1])
for i in range(len(stack)-1,-1,-1):
    print(stack[i],end="")