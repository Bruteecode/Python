# n=int(input())
n=10
for i in range(1,n):
    for j in range(i+1,n-i):
        print("*",end=" ")
    print("_______")  
    print("")  