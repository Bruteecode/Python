#adding elements to list via user- dynamic list
a=[]
n=int(input("how many elements in lists: "))
for i in range(n):
    element=int(input("Enter element: "))
    z= a.append(element)
print(z)