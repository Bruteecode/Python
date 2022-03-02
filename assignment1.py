n=int(input())
print("1")
for i in range(1,n):
    print("1",end="")
    for j in range(1,i):
        print("2",end="")
    print("1")

#for n=4
#11
#121
#1221
