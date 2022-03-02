# print all letters except except
i=0;
str="navjeet"
while i<len(str):
    if str[i]=="e":
        i+=1
        continue
    print("letter is",str[i])
    i+=1