str="hello,I am Akash.I am die-hard fan of MsDhoni.I study in CUIET"
lower=0
upper=0
vowel=0
for i in str:
    if(i>="a" and i<="z"):
        lower=lower+1
    if(i>="A" and i<="Z"):
        upper=upper+1
    if i in "aeiouAEIOU":
        vowel=vowel+1
print("Lowercase:",lower)
print("Uppercase:",upper)
print("Vowels:",vowel) 