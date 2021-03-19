from Board import Board


class Player:
    """base class of player"""

    def __init__(self, board, char, name):
        self.char = char
        self.board: Board = board
        self.name = name

    def playMove(self, coord):
        self.board.setValue(coord, self.char)
        self.board.toggleNextTurn()
