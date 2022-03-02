#sort
#listname.sort(key=function,reverse=True/False)
def sort_by_length(e):
    return len(e)
a=[3,6,9,1]
b=["abcsd","cfad","ddsaffc","fascfASVcred","yellow"]
a.sort(reverse=True)
b.sort(reverse=True,key=sort_by_length)
print(a)
print(b)