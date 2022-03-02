#filter(function,iterable)
def abc(x):
    return x>3
a=[4,5,23,11,1,2,3]
b=filter(abc,a)
print(b)
print(list(b))