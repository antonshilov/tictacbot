import re
import random

#call this function
def bot(emptyBoard):
    board = Tic()

    if (emptyBoard == ''):
        emptyBoard = "...\n...\n..."

    lb = []

    for i in emptyBoard:
        if i != "\n":
            lb.append(i)

    board.__init__(lb)

    board.show()

    fullBoard = "xox\noox\noxx"
    player = whoAmI(emptyBoard)
    board.make_move(determine(board, player), player)
    print(board.show())
    if isWon(listBoard(emptyBoard), player) == 10:
        print("I won!")
        raise NameError

    return board.show()


def nextMove(listBoard, iAm):

    if isWon(listBoard, iAm) != 0:
        return


def trustableSolution(board):

    iAm = whoAmI(board)

    for i in [5, 0, 2, 8, 10, 1, 4, 6, 9]:
        if board[i] == '.':
            board = board[:i] + iAm + board[i+1:]
            break

    return board


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


#emptyBoard = "...\n...\n..."

#fullBoard = "xox\noox\noxx"

#print(isEmptyPlaces(fullBoard))

#print(bot(emptyBoard))


class Tic(object):
    winning_combos = (
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6])

    winners = ('x-win', 'Draw', 'o-win')

    def __init__(self, squares=[]):
        if len(squares) == 0:
            self.squares = [None for i in range(9)]
        else:
            self.squares = squares

    def show(self):
        a = ''
        for i in range(0, len(self.squares)):
            #print element
            if i in [2,5]:
                a += str(self.squares[i]) + '\n'
            else:
                a += str(self.squares[i])
        return a

    def available_moves(self):
        """what spots are left empty?"""
        return [k for k, v in enumerate(self.squares) if v == '.']

    def available_combos(self, player):
        """what combos are available?"""
        return self.available_moves() + self.get_squares(player)

    def complete(self):
        """is the game over?"""
        if None not in [v for v in self.squares]:
            return True
        if self.winner() != None:
            return True
        return False

    def X_won(self):
        return self.winner() == 'x'

    def O_won(self):
        return self.winner() == 'o'

    def tied(self):
        return self.complete() == True and self.winner() is None

    def winner(self):
        for player in ('x', 'o'):
            positions = self.get_squares(player)
            for combo in self.winning_combos:
                win = True
                for pos in combo:
                    if pos not in positions:
                        win = False
                if win:
                    return player
        return None

    def get_squares(self, player):
        """squares that belong to a player"""
        return [k for k, v in enumerate(self.squares) if v == player]

    def make_move(self, position, player):
        """place on square on the board"""
        self.squares[position] = player

    def alphabeta(self, node, player, alpha, beta):
        if node.complete():
            if node.X_won():
                return -1
            elif node.tied():
                return 0
            elif node.O_won():
                return 1
            best = None
        for move in node.available_moves():
            node.make_move(move, player)
            val = self.alphabeta(node, get_enemy(player), alpha, beta)
            node.make_move(move, None)
            if player == 'O':
                if val > best:
                    best = val
            else:
                if val < best:
                    best = val
            return best

    def returnboard(self):
        a = ''
        for i in range(len(self.squares)):
            a += self.squares[0]
            if i in [2,5]:
                a += '\n'
        return a


def determine(board, player):
    a = -2
    choices = []
    if len(board.available_moves()) == 9:
        return 4
    for move in board.available_moves():
        board.make_move(move, player)
        val = board.alphabeta(board, get_enemy(player), -2, 2)
        board.make_move(move, '.')
        if val > a:
            a = val
            choices = [move]
        elif val == a:
            choices.append(move)
    return random.choice(choices)


def get_enemy(player):
    if player == 'x':
        return 'o'
    return 'x'


