#linear_search 
def linear_search(l1,key,n):
    for i in range(n):
        if(l1[i]==key):
            return 1
    return -1
l1=[3,4,13,5,6,7,9]
key=int(input("search: "))
n=len(l1)
x=linear_search(l1,key,n)
if x==1:
    print("Element found")
else:
    print("Element not found")