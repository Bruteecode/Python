#print the pattren                                            
#1    2   3    4   5
# 11   12  13   14  15
#21   22  23   24  25
#16   17  18   19  20
# 6    7    8   9   10
n=int(input())
count=0
for i in range(1,(n+1)//2+1):
     start=count*n+1
     for j in range(1,n+1):
         print(start,end=" ")
         start=start+1
     count=count+2
     print()
        
if(n%2==0):
    count(n-1)
else:
    count=n-2
for i in range(1,(n-(n+1)//2)+1):
         start=count*n+1
         for j in range(1,n+1):
                 print(start,end=" ")
                 start=start+1
         count=count-2
         print()