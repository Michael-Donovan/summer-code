def makeboard(board):
    for i in range(8):
        board.append([])
        for p in range(8):
            board[i].append("[ ]")
def printBoard(board):
    print("  A  B  C  D  E  F  G  H")
    for i in range(len(board)):
        print(i+1,end="")
        for x in range(len(board)):
            print(board[i][x], end="")
        print()
def placement(length,direction,xcoords, boards, ycoords):
    if direction=="right":
        for i in range(length):
            
board=[]
makeboard(board)
printBoard(board)