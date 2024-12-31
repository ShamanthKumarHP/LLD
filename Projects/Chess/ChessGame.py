from ChessBoard import ChessBoard

class ChessGame:
    def __init__(self):
        self.board = None
        self.player1 = None
        self.player2 = None
    
    def addPlayer1(self, player):
        self.player1 = player
    
    def addPlayer2(self, player):
        self.player2 = player
    
    def initialiseGame(self):
        self.board = ChessBoard()
    