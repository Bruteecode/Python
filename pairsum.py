rom sys import stdin


def pairSum(arr, n, x) :
    #Your code goes here
    sum=0
    for i in range(n):
        for j in range(i+1,n):
            if arr[i]+arr[j]==x:
               sum=sum+1
    return sum



#Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().strip())
    if n == 0 :
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


#main
t = int(stdin.readline().strip())

while t > 0 :
    
    arr, n = takeInput()
    x = int(stdin.readline().strip())
    print(pairSum(arr, n, x))

    t -= 1