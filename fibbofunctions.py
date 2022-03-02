# fibbonacci series 
import math
def PerfectSquare(x):
    s=int(math.sqrt(x))
    return s*s==x

n=int(input())
result1=5*(n*n)+4
result2=5*(n*n)-4

if PerfectSquare(result1) or PerfectSquare(result2):
   print(n,"true")
else:
    print(n,"false")