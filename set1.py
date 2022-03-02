#sets-mutable nature,unordered,can not take duplicate values
a=set() #empty set
b={1,22,33,1,11,1,1,1,12,22,334,334,3,4,565,334,111,223,11}
for i in b:
    print(i)#all duplicate values will be erased and only one orignal value will be taken
#set using for loop