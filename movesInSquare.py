moves = 0
#Horribly inefficient code that did not work at all.
def move(movesRight, movesDown, size):
    global moves
    if (movesRight == size) and (movesDown == size):
        moves+=1
    elif (movesRight == size):
        move(movesRight, movesDown+1, size)
    elif (movesDown == size):
        move(movesRight+1, movesDown, size)
    else:
        move(movesRight+1, movesDown, size)
        move(movesRight, movesDown+1, size)

def resetToZero():
    global moves
    moves = 0

def checkMoves(size):
    global moves
    resetToZero()
    move(0, 0, size)
    print moves
