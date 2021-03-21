f=open("/home/vedant/program files/Project-Euler/81/p081_matrix.txt", "r")
s=" "
mat=[]
while s:
    if s==' ':
        s=f.readline()
    temp=s.split(',')
    if temp[-1][-1:]=='\n':
        temp[-1]=temp[-1][:-1]
    #print(temp,'temp')
    temp=list(map(int,temp))
    mat+=[temp]
    s=f.readline()
for i in range(len(mat)):
    for j in range(len(mat[0])):
        if i==0 and j==0:
            continue
        if i==0:
            mat[i][j]+=mat[i][j-1]
        elif j==0:
            mat[i][j]+=mat[i-1][j]
        else:
            mat[i][j]+=min(mat[i-1][j],mat[i][j-1])
        

print(mat[-1][-1])
    