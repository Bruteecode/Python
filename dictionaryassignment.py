#Python Data type:list
#Ques.1
a=[11,33,44,55,66]
sum=0
for i in a:
   sum=sum+i
   print(sum)

#Ques2.
def compare(a):
    ctr = 0
    for i in a:
        if len(i) > 2 and i[0] == i[-1]:
            ctr+= 1
    return ctr

a = ['abc', 'xyz', 'aba', '1221']
for i in a:
    z = compare(a)

print(z)

#Ques3.
str=input("enter strings : ")

a=str.split(" ")

b=[]

n=int(input("enter value of n "))

for i in a:

    if (len(i)> n) :

        b.append(i)

print("list of words : ",b)





#Ques.4
a={1,2,3,4,5}
b={1,2,3}
print(a-b) 

#Python Data type:Dictionary
#Ques1.
dic1={1:10, 2:20}  
dic2={3:30, 4:40}  
dic3={5:50,6:60}  
dic4 = {}  
for d in (dic1, dic2, dic3): 
  dic4.update(d)  
print(dic4) 

#Ques2.
d=dict()
for x in range(1,16):
    d[x]=x**2
print(d)

#Ques4.
d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}

for i in d2 :
    if i in d1 :
        d1[ i ] = d1[ i ] +d2[ i ]
    else :
        d1[ i ] = d2[ i ]
print(d1)

