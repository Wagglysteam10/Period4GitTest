from House import *

window = GraphWin("Bomb Test", 600, 600)

def main():
    houses = []

    for i in range(50):
        house = House()
        houses.append(house)
        house.drawHouse(window)

    bomb = Bomb(window.getMouse())
    bomb.drawBomb(window)

    for i in houses:
        i.isHit(bomb)

    window.getMouse()
    window.close()
main()

