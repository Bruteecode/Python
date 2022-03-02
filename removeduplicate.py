#sum of elements in a list
#take two list and return the common elements from both the list
#program to remove all duplicate elements
a=[2,3,4,5,4,4,4,3,3,3,5,5]
b=[]
for i in a:
    if i not in b:
        b.append(i)
print(b)