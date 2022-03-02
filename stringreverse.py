from sys import stdin


def reverseEachWord(string):
    a=string.split()
    for i in a:
           print(i[::-1],end=" ")
    return ''
string=stdin.readline().strip()

ans=reverseEachWord(string)
print(ans)