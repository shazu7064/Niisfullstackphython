for no in range(1,1001,1):
    d=1
    s=0
    while d<=no//2:
        if no %d==0:
           s=s+d
        d=d+1
    if no==s:
      print(no,"is perfect number")