from functools import reduce
b=map(lambda x:x+x,filter(lambda x:x>2,[2,3,4,5]))
a=reduce(lambda x,y:x+y,b)
print(a)