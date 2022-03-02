str="Hi,my name is Akash chopra,I study in CUIET,my University ID is 2110991628"
lower=0
upper=0
vowels=0
digit=0
for i in str:
    if i.islower():
      lower=lower+1
    if i.isupper():
      upper=upper+1
    if i in "aeiouAEIOU":
      vowels=vowels+1
    if i.isdigit():
      digit=digit+1
print("Lowercase=",lower)
print("Uppercase=",upper)
print("Vowels=",vowels)
print("No. of digits=",digit)