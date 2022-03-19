import sys
from enum import Enum
class dir(Enum):
    east = 1
    west = 2
    north = 3
    south = 4
    def returnDir(self):
        return self.name
    def returnNum(self):
        return self.value

class dice():
    def __init__(self, pos):

        self.pos = pos

        self.upSide = 0
        self.eastSide = 0
        self.downSide = 0
        self.westSide = 0
        self.northSide = 0
        self.southSide = 0

    def changeDice(self):
        if myMap[self.pos[0]][self.pos[1]] == 0:
            myMap[self.pos[0]][self.pos[1]] = self.downSide
        else:
            self.downSide = myMap[self.pos[0]][self.pos[1]]
            myMap[self.pos[0]][self.pos[1]] = 0

    def rollEast(self):
        if self.movePos(dir.east):


            temp = self.upSide
            self.upSide = self.westSide
            self.westSide = self.downSide
            self.downSide = self.eastSide
            self.eastSide = temp
            self.changeDice()
            return True
        else: return False

    def rollWest(self):
        if self.movePos(dir.west):


            temp = self.upSide
            self.upSide = self.eastSide
            self.eastSide = self.downSide
            self.downSide = self.westSide
            self.westSide = temp

            self.changeDice()
            return True
        else: return False

    def rollNorth(self):
        if self.movePos(dir.north):

            temp = self.upSide
            self.upSide = self.southSide
            self.southSide = self.downSide
            self.downSide = self.northSide
            self.northSide = temp

            self.changeDice()

            return True
        else: return False

    def rollSouth(self):
        if self.movePos(dir.south):


            temp = self.upSide
            self.upSide = self.northSide
            self.northSide = self.downSide
            self.downSide = self.southSide
            self.southSide = temp

            self.changeDice()

            return True
        else: return False

    def checkPosMove(self, dir):
        dx = [0,0,-1,1]
        dy = [1,-1,0,0]

        if dir == dir.east:
            new_pos = (self.pos[0] + dx[0], self.pos[1] + dy[0])
        elif dir == dir.west:
            new_pos = (self.pos[0] + dx[1], self.pos[1] + dy[1])
        elif dir == dir.north:
            new_pos = (self.pos[0] + dx[2], self.pos[1] + dy[2])
        elif dir == dir.south:
            new_pos = (self.pos[0] + dx[3], self.pos[1] + dy[3])

        if new_pos[0] >= 0 and new_pos[0] <= n-1 and new_pos[1] >= 0 and new_pos[1] <= m-1:
            return True
        else:
            return False

    def printDice(self):
        print(" ", self.northSide, " ")
        print(self.westSide, self.upSide, self.eastSide)
        print(" ", self.southSide, " ")
        print(" ", self.downSide, " ")

    def movePos(self, dir):

        if dir == dir.north and self.checkPosMove(dir):
            self.pos = (self.pos[0] - 1, self.pos[1])
        elif dir == dir.south and self.checkPosMove(dir):
            self.pos = (self.pos[0] + 1, self.pos[1])
        elif dir == dir.east and self.checkPosMove(dir):
            self.pos = (self.pos[0], self.pos[1] + 1)
        elif dir == dir.west and self.checkPosMove(dir):
            self.pos = (self.pos[0], self.pos[1] - 1)
        else:
            return False

        return True

    def getPresentPos(self):
        return self.pos

    def getUpsideNum(self):
        return self.upSide

if __name__ == "__main__":
    n, m, x, y, k = map(int, sys.stdin.readline().split())

    myMap = list()
    for i in range(n):
        myMap.append(list(map(int, sys.stdin.readline().rstrip().split())))


    commandList = list(map(int, sys.stdin.readline().rstrip().split()))

    dice = dice((x,y))

    for i in commandList:
        if i == 1:
            if dice.rollEast():
                print(dice.getUpsideNum())
        elif i == 2:
            if dice.rollWest():
                print(dice.getUpsideNum())
        elif i == 3:
            if dice.rollNorth():
                print(dice.getUpsideNum())
        elif i == 4:
            if dice.rollSouth():
                print(dice.getUpsideNum())




