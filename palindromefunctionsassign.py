#(str(a)[::-1]) = Reverse String Approach
def checkpalindrome():
    return a == int(str(a)[::-1])

n=int(input())
t=n
rev=0
while n>0:
   i=n%10
   rev=(rev*10)+i
   n=n//10
if (rev==t):
    print("True")
else:
    print("False")