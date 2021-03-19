from Board import Board
from Human import Human
from Bot import Bot


b = Board(3)
p1 = Bot(b, "O", "noob")
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