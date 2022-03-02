f1=open("d.txt","w")
#write and writelines
#in write-you can add single string at a time
#writelines-for multiple strings
n=int(input("How many lines do you want to add?"))
l1=[]
for i in range(n):
    b=input("Enter data: ")
    l1.append(b)
    f1.writelines(l1)
f1.close()