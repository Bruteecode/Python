n=int(input())
a=ord('A')
for i in range(n):
    for j in range(i):
        print(chr(a),end=" ")
        a=a+1
    print()