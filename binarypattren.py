#Binary pattren
n=int(input())
for i in range(n+1):
    for j in range(n-i,0,-1):
        if i in range(1,n,2):
            print(0,end="")
        if i in range(1,n,2):
            continue
        print(1,end="")
    print()