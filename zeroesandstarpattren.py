n=int(input())
 
for i in range(n):
    for j in range (i+1):
        if i==j:
           print("*",end="")
        else:
           print(0,end="")
    for love in range(n-1,i,-1):
        if i==j:
           print(0,end="")
        else:
            print("*",end="")

    for j in range(i,n+1):
        if i==j:
           print("*",end="")

    for j in range(n-1,i-1,-1):
        if i==j:
           print("*",end="")
        else:
            print(0,end="")
    for k in range(1,i+1):
        if i==j:
          print(0,end="")
        else:
             print(0,end="")
    print()