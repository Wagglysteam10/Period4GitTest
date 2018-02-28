from updatedGraphics import *

class TrainCar(object):
    def __init__(self, x, y, color, win):
        self.x = x
        self.y = y
        self.color = color

    def drawCar(self, win): # From the TrainCar
        car = Rectangle(Point(self.x, self.y), Point(self.x+150, self.y + 75))
        car.setFill(self.color)
        frontTire = Circle(Point(self.x+25, self.y + 75), 25)
        backTire = Circle(Point(self.x+125, self.y + 75), 25)
        frontTire.setFill("Black")
        backTire.setFill("Black")
        car.draw(win)
        frontTire.draw(win)
        backTire.draw(win)

class Caboose(TrainCar):
    def __init__(self, x, y, color, win):
        super(Caboose,self).__init__(x, y, color, win)

    def drawCar(self, win): #From Caboose
        super().drawCar(win)
        top = Rectangle(Point(self.x + 25, self.y - 35), Point(self.x + 125, self.y))
        top.setFill(self.color)
        top.draw(win)
        roof = Line(Point(self.x + 20, self.y - 35), Point(self.x + 130, self.y - 35))
        roof.setWidth(10)
        roof.draw(win)
        self.drawRail(win)
    def drawRail(self, win):
        rail = Line(Point(self.x , self.y+30), Point(self.x + 150, self.y+30))
        rail.setWidth(5)
        rail.draw(win)

class Locomotive(TrainCar):
    def __init__(self, x, y, color, win):
        super(Locomotive, self).__init__(x, y, color, win)

    def drawCar(self, win): #From Locomotive
        super().drawCar(win)
        self.drawFunnel(win)
        self.drawScoop(win)

    def drawScoop(self, win):
        scoop = Polygon(Point(self.x, self.y +30), Point(self.x, self.y + 75),
                        Point(self.x-40, self.y+75))
        scoop.setFill("Black")
        scoop.draw(win)

    def drawFunnel(self, win):
        rec = Rectangle(Point(self.x + 10, self.y-30), Point(self.x + 35, self.y))
        rec.setFill("Black")
        rec.draw(win)
        top = Polygon(Point(self.x + 10, self.y-30),Point(self.x, self.y - 40),
                      Point(self.x + 45, self.y - 40), Point(self.x+35, self.y - 30))
        top.setFill("Black")
        top.draw(win)

class Train(object):
    def __init__(self, win):
        self.train =[]
        self.train.append(Locomotive(100, 200, "red", win))
        self.train.append(TrainCar(275, 200, "blue", win))
        self.train.append( TrainCar(450, 200, "yellow", win))
        self.train.append(Caboose(625, 200, "red", win))
    def drawTrain(self, win):
        for i in self.train:
            i.drawCar(win)

def main():
    window = GraphWin("Train", 900, 500)
    tc = Train(window)
    tc.drawTrain(window)
    window.getMouse()
    window.close()

main()