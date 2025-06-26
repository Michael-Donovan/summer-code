def c_to_f(cew):
    return cew*9/5+32

def f_to_c(wec):
    return wec/(9/5)-32

operation=input(" what conversion would you like to do")
num= int(input("what numbers will you use"))

if operation=="f":
    c_to_f(num)
elif operation=="c":
    f_to_c(num)



