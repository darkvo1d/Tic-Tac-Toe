from Player import Player


class Human(Player):
    """Human player"""

    def __init__(self, board, char, name):
        super().__init__(board, char, name)
        self.type = "human"

    def playMove(self):
        coord = int(input("Enter cell co-ordinate: "))
        while not self.board.isValidInput(coord):
            coord = int(input("Invalid Input. Try again: "))
        super().playMove(coord)
