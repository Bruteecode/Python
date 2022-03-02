#rectangular pattren                            
n=int(input())
for i in range(1,2*n):
     k=n
     for j in range(1,2*n):
         print(k,end="")
         if j<i:
              k=k-1
         if j>=2*n-i:
            k=k+1
     print("")
#4444444
#4333334
#4322234
#4321234
#4322234
#4333334  
#4444444