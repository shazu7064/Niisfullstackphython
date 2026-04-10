#wap take person age from keyboard check eligibal vote1
print("enter a age")
age=int(input())
#print("eligibal") if age>=18 else print("not aligibal")
msg="eligibal" if age>=18 else"not eligibal"
print(msg)