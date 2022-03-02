def binarySearch(arr, n, x) :
    #Your code goes here
       low=0
       high=n-1
       mid=0
       while low<=high:
         mid=(low+high)//2
         if arr[mid]==n:
                return 1
         elif arr[mid]>n:                
                high=mid-1
         elif arr[mid]<n:
                high=mid+1
       return -1
arr=[12,24,32,39,45,50,54]
n=int(input("search: "))
x=len(arr)
y=binarySearch(arr,n,x)
if y==1:
    print("element found")
else:
    print("element not found")
 