from Player import Player
import random
from math import inf as infinity


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
            score = self.evaluate() * depth
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
        super().playMove(coord)
