import unittest
from rover import Rover, CompassPoint
from plateau import Plateau


class RoverTestCase(unittest.TestCase):
    def setUp(self):
        self.x = 9
        self.y = 5
        self.compassPoint = CompassPoint.W
        self.rover = Rover(self.x, self.y, self.compassPoint)

    def test_position(self):
        self.assertEqual(self.rover.getPosition(), "9 5 W")

    def test_move(self):
        self.rover.moveOneStep()
        self.assertEqual(self.rover.getPosition(), "8 5 W")

    def test_turnRight(self):
        self.rover.turn("R")
        self.assertEqual(self.rover.getPosition(), "9 5 N")

    def test_turnLeft(self):
        self.rover.turn("L")
        self.assertEqual(self.rover.getPosition(), "9 5 S")


class PlateauTestCase(unittest.TestCase):
    def setUp(self):
        rover1 = Rover(3, 4, CompassPoint.W)
        rover2 = Rover(2, 2, CompassPoint.N)
        self.plateau = Plateau(5, 5, [rover1, rover2])

    def test_validPositionInside(self):
        self.assertTrue(self.plateau.isCoordinateAvailable(4, 4))

    def test_invalidPositions(self):
        self.assertFalse(self.plateau.isCoordinateAvailable(6, 4))
        self.assertFalse(self.plateau.isCoordinateAvailable(4, 6))
        self.assertFalse(self.plateau.isCoordinateAvailable(-4, 4))
        self.assertFalse(self.plateau.isCoordinateAvailable(4, -4))

    def test_roverCollide(self):
        self.assertFalse(self.plateau.isCoordinateAvailable(3, 4))


if __name__ == '__main__':
    unittest.main()

