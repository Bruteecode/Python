n=int(input())
a=0
b=1
i=0
while i<n:
   i=a+b
   a=b
   b=i
   i=i+1
print(b)