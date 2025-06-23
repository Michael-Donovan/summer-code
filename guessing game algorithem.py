import random 
num=random.randint(1,100)
start=0
end=100
counter=0
while True:
    counter+=1
    guess=int((end-start)/2)+start
    if guess>num:
        end=guess-1
    elif guess<num:
        start=guess+1
    else: 
        break
counter2=0
while True:
    counter2+=1
    guess=int(input("enter a number 1/100 "))
    if guess>num:
        print("the number is lower")
    elif guess<num:
        print("the number is higher")
    else: 
        break
print(counter)
print(counter2)
if counter>counter2:
    print("player 1 has won the game")

elif counter2>counter: 
    print("player two has won the game")

else: 
    print("there has been a tie")