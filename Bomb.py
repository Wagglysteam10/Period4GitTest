from updatedGraphics import *

class Bomb(object):
    """Creates a bomb"""
    def __init__(self, center:Point, radius = 200):
        self.center = center
        self.centerX = center.getX()
        self.centerY = center.getY()
        self.radius = radius
        self.bomb = Circle(self.center, self.radius)
        self.bomb.setOutline("red")

    def drawBomb(self, win:GraphWin):
        self.bomb.draw(win)