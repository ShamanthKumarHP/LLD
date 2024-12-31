from ChessGame import ChessGame
from Player import Player

chess_demo = ChessGame()
Player1 = Player()
Player1.name = "Alice"
Player1.isCurrentPlayer = True
Player1.status = "in-game"

Player2 = Player()
Player1.name = "Bob"
Player1.isCurrentPlayer = False
Player1.status = "in-game"

chess_demo.addPlayer1(Player1)
chess_demo.addPlayer2(Player2)

chess_demo.initialiseGame()