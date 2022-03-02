def ftoc():
    S = int(input())
    E = int(input())
    W = int(input())
    while S<=E:
        C=(S-32)*(5/9)
        print(S,"\t",int(C))
        S=S+W

ftoc()