from sys import stdin


def highestOccuringChar(string) :
	#Your code goes here

 if len(string)<=2:
       return string[0]
 else:
      max=0
      me=0
      for i in string:
       c=string.count(i)
      if c>max:
            max=c
            me=i
      else:
            string=string.replace(i,'')
 return me





#main
string = stdin.readline().strip();
ans = highestOccuringChar(string)

print(ans)