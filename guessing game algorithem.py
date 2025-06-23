import random 
num=random.randint(1,100)
start=0
end=100
while True:
    guess=int(end/2+start)
    print(guess)
    if guess>num:
        print("the number is lower")
        end=guess-1
    elif guess<num:
        print("the number is higher")
        start=guess+1
    else: 
        print(" you win")
        break