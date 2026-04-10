"""wap take two nos from keyboard enter your choice 1.add 2.sub 3.mu1t invalid choice menu driven program"""
print("enter two nos")
no1=int(input())
no2=int(input())
print("enter your choice\n1.add\n2.sub\n3.mu1t")
ch=int(input())
if ch==1:
    print("sum=",no1+no2)
elif ch==2:
	print("sub=",no1-no2)
elif ch==3:
	print("mu1t=",no1*no2)
else:
	print("invalid choice")