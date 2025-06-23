import random 
num=random.randint(1,100)

while True:
    guess=int(input("enter a number 1/100 "))
    if guess>num:
        print("the number is lower")
    elif guess<num:
        print("the number is higher")
    else: 
        print(" you win")
        break