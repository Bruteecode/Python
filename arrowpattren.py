n=int(input())
n1=(n+1)//2
for i in range(n+1):
    if i<=n1:
        for space in range (i-1):
           print(" ",end="")
        for j in range(i):
            print("*",end=" ")
        print()

    else:
        for space in range (n-i):
             print(" ",end="")
        for k in range(2*n-2*i+1,0,-2):
            print("*",end=" ")
        print()