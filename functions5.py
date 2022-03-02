x=10
def a():
    x=90
    def b():
        x=20
        def c():
            x=89
            print(x)
        print(x)
    print(x)    
print(x)