
ans = ""
for n in range(2, 10):
	for i in range(1, 10**(9 // n)):
		s = "".join(str(i * j) for j in range(1, n + 1))
		if "".join(sorted(s)) == "123456789":
			ans = max(s, ans)
print(ans) 


