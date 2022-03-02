list=['abc','xyz','aba','1221']
count=0
for i in list:
  c=list.count(i)
  if c>=2 and i[0]==i[-1]:
    count=count+1
print(count)