#program to remove multiple occurance in a list
def remove_multiple(a,item):
  for i in a:
    a.remove(i)
  return a
a=[2,3,4,55,11,77,11,66,55]
item=55
print("orignal list: ", a)
x=remove_multiple(a,item) #function call
print("after deletion list is: ", x)