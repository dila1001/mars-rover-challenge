class Plateau:
    def __init__(self, x, y, rovers):
        self.x = x
        self.y = y
        self.rovers = rovers

    def isCoordinateAvailable(self, x, y):
        return self.x >= x >= 0 and self.y >= y >= 0 and not self.__roverInCoordinate(x,y)

    def __roverInCoordinate(self, x, y):
        foundRover = False
        for rover in self.rovers:
            foundRover = rover.x == x and rover.y == y
            if foundRover:
                return True

        return foundRover