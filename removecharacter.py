from sys import stdin
def removeAllOccurrencesOfChar(string, ch) :
	# Your code goes here
    b=string.replace(ch,'')
    return b
#main
string = stdin.readline().strip()
ch = stdin.readline().strip()[0]
ans = removeAllOccurrencesOfChar(string, ch)
print(ans)