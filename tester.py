n=int(input())
n1=(n+1)//2
for i in range(1,n1):
    for k in range(i,0,-1):
        print("/",end="")
    for j in range(2*i-1,n-1):
         print("*",end="")
    print("")