  x=10   #global variable
 def show():
 	global x
 	x=30
 	print(x) #30
 	return
 show()
 print(x) #30