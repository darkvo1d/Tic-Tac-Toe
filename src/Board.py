class Board:
    """Board class"""

    def __init__(self, dimension):
        self.dimension = dimension
        self.board: list = [[" " for _ in range(dimension)] for _ in range(dimension)]
        self.nextTurn = "human"  # Human always starts

    def setValue(self, coord, value):
        """makes the player of bot move on board"""
        self.board[coord // self.dimension][coord % self.dimension] = value

    def toggleNextTurn(self):
        """set the player turn"""
        if self.nextTurn == "bot":
            self.nextTurn = "human"
        else:
            self.nextTurn = "bot"

    def emptyCells(self):
        cells = []
        for x, row in enumerate(self.board):
            for y, cell in enumerate(row):
                if cell == " ":
                    cells.append([x, y])

        return cells

    def isPlayable(self):
        """checks if the game is over"""
        if self.wins("X", False):
            print("X WINS")
            return False
        elif self.wins("O", False):
            print("O WINS")
            return False
        elif len(self.emptyCells()) == 0:
            print("DRAW")
            return False
        return True

    def wins(self, char, state):
        """return False if any player has won"""
        if not state:
            state = self.board

        winState = [
            [state[0][0], state[0][1], state[0][2]],
            [state[1][0], state[1][1], state[1][2]],
            [state[2][0], state[2][1], state[2][2]],
            [state[0][0], state[1][0], state[2][0]],
            [state[0][1], state[1][1], state[2][1]],
            [state[0][2], state[1][2], state[2][2]],
            [state[0][0], state[1][1], state[2][2]],
            [state[2][0], state[1][1], state[0][2]],
        ]
        return [char, char, char] in winState

    def isValidInput(self, coord):
        """checks if the user input is valid"""
        return self.board[coord // self.dimension][coord % self.dimension] == " "

    def showOrientation(self):
        """visually shows the cell orientation to player"""
        head = "\n Game Board Orientation \n\n"
        returnString = ""
        counter = 0
        for i in range(self.dimension):
            for j in range(self.dimension):
                returnString += " " + str(counter) + " "
                counter += 1
                if j < self.dimension - 1:
                    returnString += "|"
            if i < self.dimension - 1:
                returnString += "\n---+---+---\n"
        print(head + returnString, "\n\n")

    def __repr__(self):
        head = "\n Game Board \n\n"
        returnString = ""
        for i in range(self.dimension):
            for j in range(self.dimension):
                returnString += " " + self.board[i][j] + " "
                if j < self.dimension - 1:
                    returnString += "|"
            if i < self.dimension - 1:
                returnString += "\n---+---+---\n"
        return head + returnString