#Lambda functions-also called as anonymous functions
#Lambda arguments:operation/expression
#def a(a,b,c)
# return a+b+c 

#c=a(1,2,3)
#print(c)

#x=lambda a,b: a*b+10
#print(x(2,101))

def a(a1,c1):
  return lambda b1,d1:a1+b1+c1+d1
c=a(10,8)
print(c(1,1))