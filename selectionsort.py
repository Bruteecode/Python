def selection_sort(l2,b):
    for i in range(b):
        min1=i
        for j in range(i+1,b):
            if l2[j]<l2[min1]:
               min1=j
            #swapping code
        l2[i],l2[min1]=l2[min1],l2[i]
    return l2
l1=[12,20,1,4,34,56,77,13]
a=len(l1)
x=selection_sort(l1,a)
print("sorted list is: ",x)
