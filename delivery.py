distance=int(input())
order=int(input())
if distance<=20 and order>250:
    print("yes we can deliver you! please tell us more about the weather")
    weather=input()
if weather=="sunny":
    print("we can deliver you in 30 min")
if weather=="rainy":
    print("we can deliver you in 60 min")
else:
    print("we can deliver you in standard delivery")