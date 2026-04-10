import pickle
f=open("xyz.dat","rb")
while T


rue:
	try:
		data=pickle.load(f)
		print(data)
	except EOFError:
		break
f.close()