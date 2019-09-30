import sys
from rover import Rover, CompassPoint
from plateau import Plateau


class ESA:
    def __init__(self, nw_coordinate, rover1Start, rover2Start):
        self.rover1 = self.initRover(rover1Start)
        self.rover2 = self.initRover(rover2Start)
        self.plateau = self.initPlateau(nw_coordinate)

    def initRover(self, startInfo):
        info = startInfo.split()
        compassPoint = CompassPoint.N;
        if info[2] == "E":
            compassPoint = CompassPoint.E
        if info[2] == "S":
            compassPoint = CompassPoint.S
        if info[2] == "W":
            compassPoint = CompassPoint.W

        return Rover(int(info[0]), int(info[1]), compassPoint)

    def initPlateau(self, nw_coordinate):
        coordinate = nw_coordinate.split()
        return Plateau(int(coordinate[0]), int(coordinate[1]), [self.rover1, self.rover2])

    def run(self, instructions):

        self.sendInstructionsToRover(instructions[0], self.rover1)
        self.sendInstructionsToRover(instructions[1], self.rover2)

    def sendInstructionsToRover(self, instructions, rover):
        for instruction in instructions:
            if instruction == "M":
                rover.moveOneStep()
                x = rover.x
                y = rover.y
                self.undoMove(rover)
                if self.plateau.isCoordinateAvailable(x, y):
                   rover.moveOneStep()
                else:
                    print("Cant move!!")

            elif instruction == "L" or instruction == "R":
                rover.turn(instruction)

    def undoMove(self, rover):
        rover.turn("L")
        rover.turn("L")
        rover.moveOneStep()
        rover.turn("L")
        rover.turn("L")

    def roverStatus(self):
        return "{}\n{}".format(self.rover1.getPosition(), self.rover2.getPosition())


if __name__ == '__main__':

    if len(sys.argv) != 2:
        print("Error only accepts one argument, filename")
        sys.exit(2)

    file = open(sys.argv[1], "r")
    instructions = file.readlines()
    file.close()

    esa = ESA(instructions[0], instructions[1], instructions[3])
    esa.run([instructions[2], instructions[4]])
    print(esa.roverStatus())
