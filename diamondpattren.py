n=int(input())
n1=(n+1)//2
for i in range(n1):
    for space in range(n1-i-1):
        print(" ",end="")
    for star1 in range(i+1):
        print("*",end="")
    for star2 in range(i):
       print("*",end="")
    print()

for i in range(n1):
    for space in range(i+1):
        print(" ",end="")
    for t in range(n1-i-1,0,-1):
        print("*",end="")
    for t1 in range(n1,i+2,-1):
        print("*",end="")
    print()