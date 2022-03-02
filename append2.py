#adding elements to list via user- dynamic list
a=[]
n=int(input("how many students are in the class: "))
print("Give introduction of you all.")
for i in range(n):
   students=input("my name is: ")
   a.append(students)
print(a)