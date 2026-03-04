print("A")
i=1
while i<5:
	print("B")
	i=i+1
	print("C")
	continue #by default
	print("D")
	print(i)


print("A")
i=1
while i<5:
	print("B")
	i=i+1
	if i>=3:
		continue
		print("C")
	print("D")
	print(i)

	
