import unittest
from numlinelib.NumberLine import NumberLine as NumLine
from numlinelib.exceptions import MissingPointsError


class Testnumlinelib(unittest.TestCase):
    """Test the methods of the NumberLine class.

    Args:
        unittest (TestCase): Boilerplate for unittest.
    """

    def test_empty_initialization(self):
        """Initialization with no args."""
        numline = NumLine()
        self.assertIsInstance(numline, NumLine)
        return

    def test_initialization(self):
        """Initialization with args."""
        points = [1, 2, 3]
        numline = NumLine(points=points)
        self.assertEqual(points, numline.points[0])
        return

    def test_max_initialization(self):
        """Max set correctly."""
        return

    def test_min_initialization(self):
        """Min set correctly."""
        return

    def test_max_set(self):
        """Max can be set manually."""
        return

    def test_min_set(self):
        """Min can be set manually."""
        return

    def test_MissingPointsError(self):
        """Attempting to make NumLine with max/min but no points should throw an error"""
        with self.assertRaises(MissingPointsError):
            pass
        return
