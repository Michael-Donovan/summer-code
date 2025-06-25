def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide (a,b):
    return a/b
def exponent (a,b):
    total=1
    for i in range(b):
        total=total*a
    return total

while True: 
    operation=input("What operation would you like to do, please use the sign of each operation and enter q if you want to quit")
    if operation=="q":
        print("thank you for using our calculator")
        break 
    while True:
        try:
            num1=int(input(" what would you like the first number to be?"))
            num2=int(input(" what would you like the second number to be?"))
            break
        except:
            print("enter a valid number")
            continue
    if operation=="+":
        print(add(num1,num2))
    
    elif operation=="-":
        print(subtract(num1,num2))

    elif operation=="*":
        print(multiply(num1,num2))

    elif operation=="/":
        print(divide(num1,num2))

    elif operation=="^":
        print(exponent(num1,num2))

    else:
        print("please enter a valid operation")

