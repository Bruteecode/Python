#shopping delivery from amazon
distance=int(input())
if distance>=0:
    print("yes we can deliver you! please tell us more about delivery charges")
    Order=int(input())
if Order>=550:
    print("we can give you a free delivery")
if Order<550:
    print("delivery of Rs.50 is charged")
else:
    print("we can deliver you in standard delivery")