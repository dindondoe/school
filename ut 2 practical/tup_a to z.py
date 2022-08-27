L1 = []
for i in range(1, 27):
	c = ""
	for j in range(0,i):
		c = c + chr(i+96)
	L1.append(c)
tup=tuple(L1)
print(tup)
