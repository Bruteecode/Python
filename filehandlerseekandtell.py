f1=open("abcd.txt","w")
f1.write("hi there!!\n")
f1.write("I am Akash\n")
f1.write("nothing")
f1.close()
f1=open("abc.txt","r")
#read(),#readline(),#readlines()
#read(no.of bites to read)
#readline-only one line reading.
#readlines-Can be use to read multiple lines.
print(f1.read(4)) #hi t
print(f1.readline(5))
#print(f1.readlines())

#seek and tell
print(f1.tell())
f1.seek(2) #reassign pointer value to 1
print(f1.tell())
print(f1.read(4))