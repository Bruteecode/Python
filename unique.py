import sys

def uniqueNumber(arr, n) :

    for i in range (n):
        for j in arr:
            a=arr.count(j)
            if a==1:
                return j























#Taking Input Using Fast I/O
def takeInput() :
    n = int(sys.stdin.readline().strip())

    if n == 0 :
        return list(), 0

    arr = list(map(int, sys.stdin.readline().strip().split()))
    return arr, n


#main
t = int(sys.stdin.readline().strip())

while t > 0 :
    
    arr, n = takeInput()
    print(uniqueNumber(arr, n))

    t -= 1
    

    
 