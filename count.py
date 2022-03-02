def count_occurence(a,x):
    return a.count(x)

a=[2,3,44,5,33,3,3,3,6,11]
x=int(input())
b=count_occurence(a,x)
print("the {} comes {} time".format(x,b))