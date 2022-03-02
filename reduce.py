#reduce
#reduce(func,iterable,initial value)
from functools import reduce
def abc(x,y):
    return x+y
a=[4,5,1,33]
b=reduce(abc,a,169)
print(b)