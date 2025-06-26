alphabet=["x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c"]
def encrypt(string):
    string=string.lower()
    letterList=[*string]
    for i in range(len(letterList)):
        for x in range(26):
            if letterList[i]==alphabet[x]:
                letterList[i]=alphabet[x+3]
                break
    string2 = ""
    for i in range(len(letterList)):
        string2+=letterList[i]
    return string2
def decrypt(string):
    string=string.lower()
    letterList=[*string]
    for i in range(len(letterList)):
        for x in range(3, 29):
            if letterList[i]==alphabet[x]:
                letterList[i]=alphabet[x-3]
                break
    string2 = ""
    for i in range(len(letterList)):
        string2+=letterList[i]
    return string2


while True:
    interface=input("what message would you like to encrypt or decrypt or quit")
    if interface==quit: 
        break
    option=input("would you like to encrypt or decrypt")
    if option=="encrypt":
        print(encrypt(interface))
    elif option=="decrypt":
        print(decrypt(interface))
    else:
       print("ur wrong get better")
