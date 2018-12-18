#9.14 Python Crash Course
from random import randint

class Dice():
    """Mimic a dice with any number of sides."""

    def __init__(self, sides):
        self.sides = sides

    def roll_dice(self):
        x = randint(1, self.sides)
        print(str(x))

#dice = Dice(6)
#dice = Dice(10)
dice = Dice(20)

for value in range(10):
    dice.roll_dice()
