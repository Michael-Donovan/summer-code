size=int(input (" how many lines on the x and y axis would you like"))
for i in range(size):
    for x in range(i+1):
        print("*  ", end="")
    print()