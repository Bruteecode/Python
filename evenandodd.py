# Sum of even and odd numbers separately
n=int(input())
i=1
es=0
os=0
while n>0:
    i=n%10
    if i%2==0:
        es=es+i
    else:
       os=os+i
    n=n//10
print(int(es),int(os))