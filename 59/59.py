'''what did i do?
step 1 divide test in 3 part (a each letter encrypts each part)
step 2 check for frequency of characters in each part
step 3 higest freq amoung all three is space
step 4 second highest is letter e
step 5 guess what letter is requeried for decryption to make sense '''

def decrypt(key):
	ans=""
	for (i,c) in enumerate(CIPHERTEXT):
		if 0==0:
			ans+=chr(key[i%3]^CIPHERTEXT[i])
		else:
			ans+="-"
	#print ans
	result=0
	for i in ans:
		result+=ord(i)
	print('result=',result)
f=open("/home/vedant/program files/Project-Euler/59/p059_cipher.txt", "r")
s=f.readline()
ans=(0,0,0)
ansscore=-10*10**9
CIPHERTEXT=list(map(int,s.split(',')))
f1={}
f2={}
f3={}
f=[f1,f2,f3]
for (i,c) in enumerate(CIPHERTEXT):
	if c in f[i%3].keys():
		f[i%3][c]+=1
	else:
		f[i%3][c]=1
a1=[]
sum1=sum(f[0].values())
for (x,y) in f[0].items():
	a1.append([y*100/sum1,x])
a1.sort(reverse=True)
for i in a1[:5]:
	print(i)
print("done 1")

a2=[]
sum2=sum(f[1].values())
for (x,y) in f[1].items():
	a2.append([y*100/sum2,x])
a2.sort(reverse=True)
for i in a2[:5]:
	print(i)
print("done 2")

print(f[2])
a3=[]
sum3=sum(f[2].values())
for (x,y) in f[2].items():
	a3.append([y*100/sum1,x])
a3.sort(reverse=True)
for i in a3[:5]:
	print(i)
print('done')
decrypt([ord('e'),ord('x'),ord('p')])


