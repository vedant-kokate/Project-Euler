import time
st=time.time()
def E(n):
    return (n+1)/2

def Var(n):
    return (n*n-1)/12

dices=(4,6,8,12,20)
e=0
var=0
ed=1
varsum=0

for dice in dices:
    e=E(dice)
    var=Var(dice)
    varsum = varsum*e*e + var*ed
    ed=ed*e 
    print(dice,e,var,varsum)
print(round(varsum,4))


print(time.time()-st,'s')