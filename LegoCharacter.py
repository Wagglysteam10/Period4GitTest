from updatedGraphics import *

class LegoCharacter(object):
    def __init__(self, win:GraphWin):
        self.head = LegoHead(win)
        self.body = LegoBody("green", win)
        self.legs = LegoLegs(win)


class LegoLegs(object):
    '''This creates the lego legs.'''
    def __init__(self, win: GraphWin):
        self.drawLeg(win, 375, 400)
        self.drawPants(win, 375, 375)

    def drawLeg(self, win: GraphWin, x, y):
        '''This draws the legs.'''

        leg = Rectangle(Point(x, y), Point(x + 75, y + 150))
        otherLeg = Rectangle(Point(x + 75, y), Point(x + 150, y + 150))
        leg.setFill('yellow')
        otherLeg.setFill('yellow')
        leg.draw(win)
        otherLeg.draw(win)

    def drawPants(self, win: GraphWin, x, y):
        '''Draws the pants.'''

        pant = Rectangle(Point(x, y), Point(x + 75, y + 125))
        otherPant = Rectangle(Point(x + 75, y), Point(x + 150, y + 125))
        pant.setFill('blue')
        otherPant.setFill('blue')
        pant.draw(win)
        otherPant.draw(win)

class LegoBody(object):

    def __init__(self, color, win:GraphWin):
        self.shirtColor = color
        self.drawTorso(win)
        self.drawArm(300,175,win)
        self.drawArm(550,175,win)

    def drawTorso(self, win:GraphWin):
        torso = Rectangle(Point(350, 150), Point(550, 375))
        torso.setFill(self.shirtColor)
        torso.draw(win)

    def drawArm(self, x, y, win:GraphWin):
        arm = Rectangle(Point(x,y), Point(x+50, y + 125))
        arm.setFill(self.shirtColor)
        arm.draw(win)
        hand = Circle(Point(x+25, y+150), 25)
        hand.setFill("yellow")
        hand.draw(win)

class LegoHead(object):
    """This creates a lego object head"""
    def __init__(self, win :GraphWin):
        self.drawHead(win)
        self.drawEyes(win)
        self.drawMouth(win)

    def drawHead(self, win: GraphWin):
        head = Rectangle(Point(400, 50), Point(500, 150))
        top = Rectangle(Point(425,25), Point(475,50))
        head.setFill("yellow")
        top.setFill("yellow")
        head.draw(win)
        top.draw(win)

    def drawEyes(self, win:GraphWin):
        leftEye = Circle(Point(425, 85), 10)
        leftEye.setFill("black")
        leftEye.draw(win)
        rightEye = Circle(Point(475, 85), 10)
        rightEye.setFill("black")
        rightEye.draw(win)

    def drawMouth(self, win:GraphWin):
        mouth = Line(Point(425, 125), Point(475, 125))
        mouth.setWidth(3)
        mouth.draw(win)


def main():
    window = GraphWin("LegoCharacter", 900, 800)
    legoMan = LegoCharacter(window)
    window.getMouse()
    window.close()

main()