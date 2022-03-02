#map(function,*iterable)
#map return map object
#function will take arguments as per list
def abc(x,y):
    return x**y
a=map(abc,[1,2,3,4],[1,2,1,2])
print(a)
print(tuple(a))