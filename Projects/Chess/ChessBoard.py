from Spot import Spot

class ChessBoard:
    def __init__(self):
        self.board = [[Spot() for i in range(8)] for j in range(8)]

    def resetBoard(self):
        self.board = ChessBoard()
    
    def getSpot(self, x, y):
        return self.board[x][y]
        