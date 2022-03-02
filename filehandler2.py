f1=open("c.txt","w")
#write and writelines
#in write-you can add single string at a time
#writelines-for multiple strings
n=int(input("How many lines do you want to add?"))
for i in range(n):
    b=input("Enter data: ")
    f1.write(b)
f1.close()