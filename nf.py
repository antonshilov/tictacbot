def isWin(board):
    """
    GIven a board checks if it is in a winning state.
    Arguments:
          board: a list containing X,O or -.
    Return Value:
           True if board in winning state. Else False
    """
    ### check if any of the rows has winning combination
    for i in range(3):
        if len(set(board[i*3:i*3+3])) is  1 and board[i*3] is not '.': return True
    ### check if any of the Columns has winning combination
    for i in range(3):
       if (board[i] is board[i+3]) and (board[i] is  board[i+6]) and board[i] is not '.':
           return True
    ### 2,4,6 and 0,4,8 cases
    if board[0] is board[4] and board[4] is board[8] and board[4] is not '.':
        return  True
    if board[2] is board[4] and board[4] is board[6] and board[4] is not '.':
        return  True
    return False


def nextMove(board,player):
    """
    Computes the next move for a player given the current board state and also
    computes if the player will win or not.
    Arguments:
        board: list containing X,- and O
        player: one character string 'X' or 'O'
    Return Value:
        willwin: 1 if 'X' is in winning state, 0 if the game is draw and -1 if 'O' is
                    winning
        nextmove: position where the player can play the next move so that the
                         player wins or draws or delays the loss
    """
    ### when board is '---------' evaluating next move takes some time since
    ### the tree has 9! nodes. But it is clear in that state, the result is a draw
    if len(set(board)) == 1: return 0,4

    nextplayer = 'x' if player=='o' else 'o'
    if isWin(board) :
        if player is 'x': return -1,-1
        else: return 1,-1
    res_list=[] # list for appending the result
    c= board.count('.')
    if  c is 0:
        return 0,-1
    _list=[] # list for storing the indexes where '-' appears
    for i in range(len(board)):
        if board[i] == '.':
            _list.append(i)
    #tempboardlist=list(board)
    for i in _list:
        board[i]=player
        ret,move=nextMove(board,nextplayer)
        res_list.append(ret)
        board[i]='.'
    if player is 'x':
        maxele=max(res_list)
        return maxele,_list[res_list.index(maxele)]
    else :
        minele=min(res_list)
        return minele,_list[res_list.index(minele)]

import re

#call this function
def bot(emptyBoard):

    if (emptyBoard == ''):
        emptyBoard = "...\n...\n..."

    lb = []

    for i in emptyBoard:
        if i != "\n":
            lb.append(i)


    player = whoAmI(emptyBoard)

    i = nextMove(lb, player)

    if isWon(listBoard(emptyBoard), player) == 10:
        print("I won!")
        raise NameError

    eB = ''

    if i[1] in [0,1,2]:
        eB = emptyBoard[:i[1]] + player + emptyBoard[i[1]+1:]
    elif i[1] > 2 and i[1] <=5:
        eB = emptyBoard[:i[1]+1] + player + emptyBoard[i[1]+2:]
    elif i[1] > 5:
        eB = emptyBoard[:i[1]+2] + player + emptyBoard[i[1]+3:]

    return eB


def listBoard(board):
    return board.split("\n")


def runner():
    #newState = bot(board)
    #print(newState)
    pass


def isWon(listBoard, iAm):

   if (listBoard[0][0] == listBoard[0][1] and listBoard[0][1] == listBoard[0][2] and listBoard[0][2] != '.'):
       if listBoard[0][0] == iAm:
           return 10
       else:
           return -10
   elif (listBoard[1][0] == listBoard[1][1] and listBoard[1][1] == listBoard[1][2] and listBoard[1][2] != '.'):
       if listBoard[1][0] == iAm:
           return 10
       else:
           return -10
   elif (listBoard[2][0] == listBoard[2][1] and listBoard[2][1] == listBoard[2][2] and listBoard[2][2] != '.'):
       if listBoard[2][0] == iAm:
           return 10
       else:
           return -10
   elif (listBoard[0][0] == listBoard[1][0] and listBoard[1][0] == listBoard[2][0] and listBoard[2][0] != '.'):
       if listBoard[0][0] == iAm:
           return 10
       else:
           return -10
   elif (listBoard[0][1] == listBoard[1][1] and listBoard[1][1] == listBoard[2][1] and listBoard[2][1] != '.'):
       if listBoard[0][1] == iAm:
           return 10
       else:
           return -10
   elif (listBoard[0][2] == listBoard[1][2] and listBoard[1][2] == listBoard[2][2] and listBoard[2][2] != '.'):
       if listBoard[0][2] == iAm:
           return 10
       else:
           return -10
   elif (listBoard[0][0] == listBoard[1][1] and listBoard[1][1] == listBoard[2][2] and listBoard[2][2] != '.'):
       if listBoard[0][0] == iAm:
           return 10
       else:
           return -10
   elif (listBoard[0][2] == listBoard[1][1] and listBoard[1][1] == listBoard[2][0] and listBoard[2][0] != '.'):
       if listBoard[0][2] == iAm:
           return 10
       else:
           return -10
   else:
       return 0

def isEmptyPlaces(board):

    isEmpty = False

    if board.count(".") != 0:
        isEmpty = True

    return isEmpty


def whoAmI(board):

    x = board.count("x")
    o = board.count("o")

    if x == o:
        iAm = 'x'
    else:
        iAm = 'o'

    if x < o or x - o > 1:
        raise ValueError

    if not isEmptyPlaces(board):
        raise ValueError

    if not re.search(pattern="^[xo.]{3}\n[xo.]{3}\n[xo.]{3}$", string=board,):
        raise ValueError

    if isWon(listBoard(board), iAm) != 0:
        raise NameError

    return iAm

#print(bot('xxo\nxo.\n...'))