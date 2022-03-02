#dictionary comprehension and zip
a=[1,2,3,4,5]
b=[6,7,8,9,1]
c={i:j for i,j in zip(a,b)}
print(c)
