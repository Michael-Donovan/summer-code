cart=[]
store=["videogames", "cheese", "burgers", "chocolate", "candy", "water", "juice"]
while True:
    option=input("would you like to add a item to the basket click A, remove a item from the basket click S, or finish shopping click M")
    if option=="A":
        for i in range(len(store)):
            print(i+1,": ",store[i])
        choice = int(input("what number item do you want"))
        cart.append(store[choice-1])
        print(cart)
    elif option=="S":
        for i in range(len(cart)):
            print(i+1,": ",cart[i])
        choice2=int(input("choose what numbered item do you want to get rid of"))
        store.append(cart[choice2-1])
        cart.remove(cart[choice2-1])
        print(cart)
    elif option=="M":
        print("How much would you like to tip 10 percent 20 percent or 60 percent")
        break