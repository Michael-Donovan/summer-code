def display(board):
    print(board[0][0],"|",board[0][1],"|",board[0][2])
    print("---------")
    print(board[1][0],"|",board[1][1],"|",board[1][2])
    print("---------")
    print(board[2][0],"|",board[2][1],"|",board[2][2])

board=[]
for i in range(3):
    board.append([" "," "," "])
turnCounter=0
while True:
    display(board)
    turnCounter+=1
    if turnCounter%2==0:
        while True:
            omove=input("what move would you like to make ")
            placement=omove.split(",")
            print (placement)
            placement[0] = int(placement[0])
            placement[1] = int(placement[1])
            if int(placement[0])<=3 and int(placement[1])<=3 and board[placement[1]-1][placement[0]-1]==" ":
                board[placement[1]-1][placement[0]-1] ="O"
                break
    else:
        while True:
            move=input("what move would you like to make ")
            placement=move.split(",")
            print (placement)
            placement[0] = int(placement[0])
            placement[1] = int(placement[1])
            if int(placement[0])<=3 and int(placement[1])<=3 and board[placement[1]-1][placement[0]-1]==" ":
                board[placement[1]-1][placement[0]-1]="x"
                break
    
    
