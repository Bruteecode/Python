#map(function,*list)
#map return map object
#function will take arguments as per list
def abc(x):
   return x+2
a=map(abc,[1,2,3,4])
print(a)
print(list(a))