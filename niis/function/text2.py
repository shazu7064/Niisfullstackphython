x=30 #global variable
def show():
	x=30 #local variable
	print(x) #30
	return
	show()
	print(x) #10