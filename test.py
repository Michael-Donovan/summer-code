 if board[0][1]=="x" and board[1][1]=="x" and board[2][1]=="x":
        display(board)
        print("you win")
        break
    if board[0][0]=="x" and board[1][0]=="x" and board[2][0]=="x":
        display(board)
        print("you win")
        break
    if board[0][2]=="x" and board[1][2]=="x" and board[2][2]=="x":
        display(board)
        print("you win")
        break

    if board[0][1]=="x" and board[0][0]=="x" and board[0][2]=="x":
        display(board)
        print("you win")
        break
    if board[1][0]=="x" and board[1][1]=="x" and board[1][2]=="x":
        display(board)
        print("you win")
        break
    if board[2][0]=="x" and board[2][1]=="x" and board[2][2]=="x":
        display(board)
        print("you win")
        break

    if board[0][0]=="x" and board[1][1]=="x" and board[2][2]=="x":
        display(board)
        print("you win")
        break
    if board[0][2]=="x" and board[1][1]=="x" and board[2][0]=="x":
        display(board)
        print("you win")
        break


