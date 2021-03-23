import time
st=time.time()
f=open("/home/vedant/program files/Github/vedantkokate07/Project-Euler/89/p089.txt", "r")

def printRoman(number):
	ans=''
	num = [1, 4, 5, 9, 10, 40, 50, 90, 	100, 400, 500, 900, 1000]
	sym = ["I", "IV", "V", "IX", "X", "XL",	"L", "XC", "C", "CD", "D", "CM", "M"]
	i = 12
	while number:
		div = number // num[i]
		number %= num[i]

		while div:
			ans+=sym[i]
			div -= 1
		i -= 1
	return ans


def value(r):
	if (r == 'I'):
		return 1
	if (r == 'V'):
		return 5
	if (r == 'X'):
		return 10
	if (r == 'L'):
		return 50
	if (r == 'C'):
		return 100
	if (r == 'D'):
		return 500
	if (r == 'M'):
		return 1000
	return -1


def romanToDecimal(str):
	res = 0
	i = 0

	while (i < len(str)):

		# Getting value of symbol s[i]
		s1 = value(str[i])

		if (i + 1 < len(str)):

			# Getting value of symbol s[i + 1]
			s2 = value(str[i + 1])

			# Comparing both values
			if (s1 >= s2):

				# Value of current symbol is greater
				# or equal to the next symbol
				res = res + s1
				i = i + 1
			else:

				# Value of current symbol is greater
				# or equal to the next symbol
				res = res + s2 - s1
				i = i + 2
		else:
			res = res + s1
			i = i + 1

	return res


ans=0
for i in range(1000):
    s=f.readline().strip()
    num=romanToDecimal(s)
    roman=printRoman(num)

    ans+=len(s)-len(roman)
print(ans)
print(time.time()-st,'s')