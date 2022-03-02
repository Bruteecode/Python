n=int(input())
for i in range(1,n+1):
    for k in range(1,n-i+1):
        print(" ",end="")
    for j in range(i):
        print("*",end="")
    for  p in range(2,i+1):
        print("*",end="")
    print("")