from statistics import mean
import math
from typing import Any

class Dragon():
    def __init__(self,height,fire,colour):
        self.height =  height
        self.fire = fire
        self.colour = colour
    
    def __eq__(self,other):
        if self.height == other.height and self.fire == other.fire and self.colour == other.colour:
            return True
        else:
            return False

    def __lt__(self,other):
        selfPoint = 0
        otherPoint = 0
        if self.height < other.height:
            selfPoint = selfPoint + 1
        elif self.height == other.height:
            selfPoint = selfPoint + 1
            otherPoint = otherPoint + 1
        else:
            otherPoint = otherPoint + 1
        if self.fire < other.fire:
            selfPoint = selfPoint + 1
        elif self.fire == other.fire:
            selfPoint = selfPoint + 1
            otherPoint = otherPoint + 1
        else:
            otherPoint = otherPoint + 1
        if self.colour < other.colour:
            selfPoint = selfPoint + 1
        elif self.colour == other.colour:
            selfPoint = selfPoint + 1
            otherPoint = otherPoint + 1
        else:
            otherPoint = otherPoint + 1
        if selfPoint > otherPoint:
            return True
        else:
            return False
    
    def __gt__(self,other):
        selfPoint = 0
        otherPoint = 0
        if self.height > other.height:
            selfPoint = selfPoint + 1
        elif self.height == other.height:
            selfPoint = selfPoint + 1
            otherPoint = otherPoint + 1
        else:
            otherPoint = otherPoint + 1
        if self.fire > other.fire:
            selfPoint = selfPoint + 1
        elif self.fire == other.fire:
            selfPoint = selfPoint + 1
            otherPoint = otherPoint + 1
        else:
            otherPoint = otherPoint + 1
        if self.colour > other.colour:
            selfPoint = selfPoint + 1
        elif self.colour == other.colour:
            selfPoint = selfPoint + 1
            otherPoint = otherPoint + 1
        else:
            otherPoint = otherPoint + 1
        if selfPoint > otherPoint:
            return True
        else:
            return False
            
    def __le__(self,other):
        selfPoint = 0
        otherPoint = 0
        if self.height <= other.height:
            selfPoint = selfPoint + 1
        else:
            otherPoint = otherPoint + 1
        if self.fire <= other.fire:
            selfPoint = selfPoint + 1
        else:
            otherPoint = otherPoint + 1
        if self.colour <= other.colour:
            selfPoint = selfPoint + 1
        else:
            otherPoint = otherPoint + 1
        if selfPoint > otherPoint:
            return True
        else:
            return False
        
    def __ge__(self,other):
        selfPoint = 0
        otherPoint = 0
        if self.height >= other.height:
            selfPoint = selfPoint + 1
        else:
            otherPoint = otherPoint + 1
        if self.fire >= other.fire:
            selfPoint = selfPoint + 1
        else:
            otherPoint = otherPoint + 1
        if self.colour >= other.colour:
            selfPoint = selfPoint + 1
        else:
            otherPoint = otherPoint + 1
        if selfPoint > otherPoint:
            return True
        else:
            return False

    def __add__(self,other):
        height2 = (self.height + other.height)/2
        if self.fire > other.fire:
            fire2 = self.fire
        else:
            fire2 = other.fire
        colour2 = [self.colour,other.colour]
        colour2 = sorted(colour2)[0]
        NewDragon = height2,fire2,colour2
        return NewDragon
    
    def __sub__(self, number):
         self.height = self.height - int(self.height / number)
         self.fire = self.fire + self.fire % number
         return self

    def __repr__(self) -> str:
        return f'Dragon with height {self.height}, danger {self.fire} and color {self.colour}'
        
    
    def str(self):
        return f'Dragon {self.height}, {self.fire}, {self.colour} '
    
    def __call__(self,other):
        string = ""
        for i in range(self.fire):
            string = string + other
        return string

    def change_colour(self,other):
        self.colour = other

dr = Dragon(69, 5, "brown")
dr1 = Dragon(69, 5, "gray")

print (dr > dr1, dr != dr1, dr <= dr1)
print(dr, dr1, sep="\n")
print()

dr.change_colour("white")
dr -= 23
dr1 -= 2
dr2 = dr+dr1
print(dr, dr1, dr2, sep="\n")
print(dr("Welcome"))