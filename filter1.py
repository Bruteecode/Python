#filter (function,iterable)
def abc(x):
    return x%2!=0
a=[4,5,1,33,2,3,6,7]
b=filter(abc,a)
print(b)
print(tuple(b))