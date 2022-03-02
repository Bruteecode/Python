from sys import stdin

def removeConsecutiveDuplicates(string) :
	# Your code goes here
  chars=[]
  prev=None
    
  for c in string:
    if prev!=c:
        chars.append(c)
        prev=c
        
  return ''.join(chars)


























	


#main
string = stdin.readline().strip()

ans = removeConsecutiveDuplicates(string)

print(ans)