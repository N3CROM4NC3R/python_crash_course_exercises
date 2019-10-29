from random import randint

class Dice():
    def __init__(self,sides=6):
        self.sides = sides

    def roll_dice(self):
        print(randint(0,self.sides))

sided_10 = Dice(10)
sided_20 = Dice(20)

for i in range(10):
    print("Dice 1:")
    sided_10.roll_dice()
    print("Dice 2:")
    sided_20.roll_dice()