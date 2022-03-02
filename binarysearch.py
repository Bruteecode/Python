#binary search
def binary_search(l1,key,n):
        low=0
        high=n-1
        mid=0
        while low<=high:
          mid=(low+high)//2
          if l1[mid]==key:
                return 1
          elif l1[mid]>key:
                high=mid-1
          elif l1[mid]<key:
                high=mid+1
        return -1
l1=[12,24,32,39,45,50,54]
key=int(input("search: "))
n=len(l1)
x=binary_search(l1,key,n)
if x==1:
    print("element found")
else:
    print("element not found")