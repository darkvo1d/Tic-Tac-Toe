from math import inf as infinity


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


class Player:
    """base class of player"""

    def __init__(self, board, char, name):
        self.char = char
        self.board: Board = board
        self.name = name

    def playMove(self, coord):
        self.board.setValue(coord, self.char)
        self.board.toggleNextTurn()


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


class Bot(Player):
    """Bot player"""

    def __init__(self, board, char, name):
        super().__init__(board, char, name)
        self.type = "bot"
        self.state = self.board.board.copy()
        self.opponentChar = "O"

    def emptyCells(self):
        cells = []
        for x, row in enumerate(self.state):
            for y, cell in enumerate(row):
                if cell == " ":
                    cells.append([x, y])
        return cells

    def evaluate(self):
        """returns +1 if the computer wins; -1 if the human wins; 0 draw"""
        if self.board.wins(1, self.state):
            score = +1
        elif self.board.wins(-1, self.state):
            score = -1
        else:
            score = 0

        return score

    def minimax(self, state, player, depth=8):
        """
        AI function that choice the best move
        :param state: current state of the board
        :param depth: node index in the tree (0 <= depth <= 9) basically number of moves possible at that moment)
        :param player: an human(-1) or a computer(1)
        :return: a list with [the best row, best col, best score]
        """
        if player == 1:
            best = [-1, -1, -infinity]
        else:
            best = [-1, -1, +infinity]

        if depth == 0 or self.evaluate():
            score = depth * self.evaluate()
            if depth < 5:
                0 and print("==>" * (9 - depth), "score", score)
            return [-1, -1, score]

        for cell in self.emptyCells():
            x, y = cell[0], cell[1]
            state[x][y] = player
            if depth < 5:
                0 and print("==>" * (9 - depth), "depth = ", depth, "player = ", player, state, "cell = ", cell)
            score = self.minimax(state, -player, depth - 1)
            state[x][y] = " "
            score[0], score[1] = x, y
            if player == 1:
                if score[2] > best[2]:
                    best = score  # max value
            else:
                if score[2] < best[2]:
                    best = score  # min value

        return best

    def getCoord(self):
        depth = len(self.board.emptyCells())
        move = self.minimax(self.state, 1, depth)
        x, y = move[0], move[1]
        return abs(x * 3 + y)

    def updateState(self):
        translate = lambda cell: 1 if cell == self.char else (cell if cell == " " else -1)
        self.state = [[translate(cell) for cell in row] for row in self.board.board]

    def playMove(self):
        self.updateState()
        coord = self.getCoord()
        #print(coord)
        super().playMove(coord)


b = Board(3)
p1 = Bot(b, "O", "noob_1")
p2 = Human(b, "X", "sarvang")
b.showOrientation()
print(b)

while b.isPlayable():
    if b.nextTurn == "bot":
        print("\nBot playing ...")
        p1.playMove()
    else:
        print("\nYour turn ...")
        p2.playMove()
    print(b)