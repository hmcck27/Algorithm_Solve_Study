import sys
from enum import Enum

board = list()

class type(Enum):
    low = 1
    col = 2
    sqr = 3

for i in range(9):
    board.append([i for i in list(map(int, sys.stdin.readline().rstrip().split()))])

def checkSquare(i,j, board):

    return set()

def checkLow(i,j, board):

    return set()

def checkCol(i,j, board):

    return set()

def sdoku(board, type):

    squareSet = checkSquare()
    lowSet = checkLow()
    colSet = checkCol()

    if len(checkSquare(i,j, board)) == 1:
        board[i][j] = checkSquare(i,j, board)
    elif len(checkLow(i,j, board)) == 1:

    elif len(checkCol(i,j, board)) == 1:


sdoku(board, type.low)
