#find power of a number without ** operator
no=2
p=7
res=1
while p>0:
    print(res,end="\t")
    res=res*no
    p=p-1


no=6
d=1
s=0
while d<=no//2:
    if no %d==0:
       s=s+d 
    d=d+1
if no==s:
   print(no,"is perfect number")
else:
   print(no,"is not perfect number")


