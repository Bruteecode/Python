#method to use in place of close
with open("bbb.txt","w") as f2:
    f2.write("hello!!\n")
    f2.write("I am Akash\n")
    f2.write("hi there\n")
    f2.write("what is you name")
with open("bbb.txt","r") as f2:
    print(f2.read())