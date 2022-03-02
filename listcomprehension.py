#list comprehension
#new list=[expression for loop if condition]
#program to display a list not containing any specific value
a=["akash","ijklm","def"]
b=[]
for x in a:
    if "a" in x:
        b.append(x)
print(b)