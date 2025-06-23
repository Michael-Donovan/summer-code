import random
unknown=random.randint(0,2)
rand=["R","P","S"]
computehand=rand[unknown]
playhand=input("R,P, or S").upper()
if playhand=="R":
    if computehand=="R":
        print("tie")
    if computehand=="P":
        print("computehand wins")
    if computehand=="S":
        print("playhand wins")
if playhand=="P":
    if computehand=="P":
        print("tie")
    if computehand=="S":
        print("computehand wins")
    if computehand=="R":
        print("playhand wins")
if playhand=="S":
    if computehand=="S":
        print("tie")
    if computehand=="R":
        print("computehand wins")
    if computehand=="P":
        print("playhand wins")

