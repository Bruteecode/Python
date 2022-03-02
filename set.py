#sets-mutable nature,unordered,can not take duplicate values
a={} # empty set
b={11,22,33,44,1,11,1,1,1,11,1,1,11} #As set do not take duplicate values so its answer will be{1,11,44,22,33}
#all duplicate values will be erased and only one orignal value will be taken
print(b)