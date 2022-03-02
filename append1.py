#adding elements to list via user- dynamic list
a=[]
n=int(input("how many elements in the list: "))
for i in range(n):
    element=int(input("enter element: "))
    a.append(element)
print(a)