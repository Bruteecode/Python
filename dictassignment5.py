#write a python program to print all unique values in a dictionary
d1=[{1:45},{2:677},{3:54},{1:45},{2:677},{2:677}]
unique_values=set(a for i in d1 for a in i.items())
print(unique_values)