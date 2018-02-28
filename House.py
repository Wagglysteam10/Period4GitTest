import random
from Bomb import *
class House(object):

    def __init__(self):
        """creates a house in a random location"""
        self.x = random.randint(0, 590)
        self.y = random.randint(0, 590)
        self.size = 10
        self.home = Rectangle(Point(self.x, self.y),
            Point(self.x + self.size, self.y + self.size))
        self.home.setFill("Black")

    def drawHouse(self, win:GraphWin):
        self.home.draw(win)

    def getDistance(self, bombCenter:Point):
        houseCenter = self.home.getCenter()
        dx = (houseCenter.getX() - bombCenter.getX())**2
        dy = (houseCenter.getY() - bombCenter.getY())**2
        return (dx + dy)**0.5

    def isHit(self, bomb:Bomb):
        if self.getDistance(bomb.center) < bomb.radius:
            self.home.setFill("red")

