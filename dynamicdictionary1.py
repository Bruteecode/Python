#method-1 to create dynamic dictionary
student_1=["name","rollno","marks"] #keys
d1={}
for i in student_1:
    val=input("Enter:")
    d1[i]=val
print(d1)