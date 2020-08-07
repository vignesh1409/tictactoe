board=[' ' for x in range(10)]
def printletter(pos,letter):
    board[pos]=letter
def printboard(board):
    print('    |    |   ')
    print('',board[1],' |',board[2],' |',board[3])
    print('    |    |   ')
    print("--------------------")
    print('    |    |   ')
    print('', board[4], ' |', board[5], ' |', board[6])
    print('    |    |   ')
    print("--------------------")
    print('    |    |   ')
    print('', board[7], ' |', board[8], ' |', board[9])
    print('    |    |   ')
    print('---------------------------------------------------')
def iswinner(b,l):
    return (b[1]==l and b[2]==l and b[3]==l)  or  (b[4]==l and b[5]==l and b[6]==l)  or (b[7]==l and b[8]==l and b[9]==l)  or  (b[1]==l and b[4]==l and b[7]==l)  or  (b[2]==l and b[5]==l and b[8]==l)  or  (b[3]==l and b[6]==l and b[9]==l) or (b[1]==l and b[5]==l and b[9]==l) or (b[3]==l and b[5]==l and b[7]==l)

def spacefree(pos):
    return board[pos]==' '
def boardfull(board):
    if board.count(" ")>1:
        return False
    else:
        return True
def playermove():
    run=True
    while run:
        move=input("Please enter the number from 1 to 9")
        try:
            move=int(move)
            if move>0 and move<10:
                if spacefree(move):
                    run=False
                    printletter(move,'X')
                else:
                    print("The space is been occupied")
            else:
                print("Please enter a valid input")
        except:
            print("Please enter a digit from 0 to 9")
def computermove():
    possiblemove=[x for x ,letter in enumerate(board) if letter ==' ' and x!=0]
    move=0
    for let in ['O','X']:
        for i in possiblemove:
            boardcopy=board[:]
            boardcopy[i]=let
            if iswinner(boardcopy,let):
                move=i
                return move
    cornerlist=[]
    for i in possiblemove:
        if i in [1,3,7,9]:
            cornerlist.append(i)
    if len(cornerlist)>0:
        move=selectrandom(cornerlist)
        return move
    if 5 in possiblemove:
        move=5
        return move
    edgelist=[]
    for i in possiblemove:
        if i in [2,4,6,8]:
            edgelist.append(i)
    if len(edgelist)>0:
        move=selectrandom(edgelist)
        return move
def selectrandom(l):
    import random
    ln=len(l)
    r=random.randrange(0,ln)
    return l[r]
def main():
    print("Welcome to the game")
    printboard(board)
    while not(boardfull(board)):
        if not(iswinner(board,'O')):
            playermove()
            printboard(board)
        else:
            print("Sorry you loose")
            break
        if not(iswinner(board,'X')):
            move=computermove()
            if move==0:
                print(" ")
            else:
                printletter(move,'O')
                printboard(board)
        else:
            print("You win")
            break


    if boardfull(board):
        print("Tie")
while True:
    s=input("do you want to play it again(Y/N):")
    if s=='Y':
        board = [' ' for x in range(10)]
        main()
    else:
        print("Oops You got bored!!")
        break


