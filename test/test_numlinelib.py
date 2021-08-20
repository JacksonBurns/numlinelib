import unittest
from numlinelib.NumberLine import NumberLine as NumLine


class Testnumlinelib(unittest.TestCase):
    """Test the methods of the NumberLine class.

    Args:
        unittest (TestCase): Boilerplate for unittest.
    """

    def test_empty_initialization(self):
        """Ensure NumberLine can be initialized with no args."""
        numline = NumLine()
        self.assertIsInstance(numline, NumLine)

    def test_initialization(self):
        """Ensure NumberLine can be initialized with args."""
        points = [1, 2, 3]
        numline = NumLine(points)
        self.assertEqual(points, numline.points[0])
