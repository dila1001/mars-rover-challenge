from enum import IntFlag


class Rover:
    def __init__(self, x, y , compassPoint):
        self.x = x
        self.y = y
        self.compassPoint = compassPoint

    def getPosition(self):
        return '{} {} {}'.format(self.x, self.y, self.compassPoint.name)

    def moveOneStep(self):
        if self.compassPoint == CompassPoint.N:
            self.y = self.y + 1
        elif self.compassPoint == CompassPoint.S:
            self.y = self.y - 1
        elif self.compassPoint == CompassPoint.E:
            self.x = self.x + 1
        elif self.compassPoint == CompassPoint.W:
            self.x = self.x - 1

    def turn(self, direction):
        newCompassPoint = self.compassPoint
        if direction == "L":
            newCompassPoint = self.compassPoint - 1
        elif direction == "R":
            newCompassPoint = self.compassPoint + 1
        self.compassPoint = CompassPoint(newCompassPoint % 4)


class CompassPoint(IntFlag):
    N = 0,
    E = 1,
    S = 2,
    W = 3,
