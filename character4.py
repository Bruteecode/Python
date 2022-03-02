n=int(input())
a=ord('A')
for i in range(n+1):
    for j in range(4,0,-1):
        print(chr(a),end="")
        a=a+1
    print()