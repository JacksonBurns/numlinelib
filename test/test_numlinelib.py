import unittest

import matplotlib.pyplot as plt

from numlinelib.NumberLine import NumberLine as NumLine
from numlinelib.exceptions import (
    MissingPointsError,
    MultidimensionalPointsError,
    InvalidLimitError,
)


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

    def test_args_initialization(self):
        """Initialize number line without using keyword args."""
        points = [1, 2, 3]
        numline = NumLine(points, show=False)
        self.assertEqual(points, numline.get_points())

    def test_partial_initialization(self):
        """Initialization with some args."""
        points = [1, 2, 3]
        numline = NumLine(points=points, show=False)
        self.assertEqual(points, numline.get_points())
        return

    def test_full_initialization(self):
        """Initialization with all args."""
        points = [1, 2, 3]
        mn = 0
        mx = 4
        numline = NumLine(points=points, min=mn, max=mx, show=False)
        self.assertEqual(points, numline.get_points())
        return

    def test_min_initialization(self):
        """Initialization with all args."""
        points = [1, 2, 3]
        mn = 0
        mx = 4
        numline = NumLine(points=points, min=mn, max=mx, show=False)
        self.assertEqual(mn, numline.get_min())
        return

    def test_max_initialization(self):
        """Initialization with all args."""
        points = [1, 2, 3]
        mn = 0
        mx = 4
        numline = NumLine(points=points, min=mn, max=mx, show=False)
        self.assertEqual(mx, numline.get_max())
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

    def test_calc_min(self):
        """Initializing with points=[1,2,3] should make the min 0"""
        return

    def test_calc_max(self):
        """Initializing with points=[1,2,3] should make the max 4"""
        return

    def test_2d_list_sanitize(self):
        """Attempting to enter points that are not 1D should throw an exception"""
        return

    def test_numpy_sanitize(self):
        """Points provided as numpy array should be converted to list by NumberLine"""
        return

    def test_pandas_sanitize(self):
        """Points provided as pandas dataframe should be converted to a list by NumberLine"""
        return

    def test_invalid_max(self):
        """Setting max lower than min should raise an InvalidLimitError"""
        return

    def test_invalid_min(self):
        """Setting min higher than max should raise an InvalidLimitError"""
        return

    def test_point_marker(self):
        """Calling with a marker specified should set that marker."""
        return

    def test_point_size(self):
        """Calling with a point size should set that size."""
        return

    def test_min_ticks_error(self):
        """Setting ticks that have a minimum lower than the minimum of the plot should raise an InvalidLimitError."""
        return

    def test_mmax_ticks_error(self):
        """Setting ticks that have a maximum higher than the maximum of the plot should raise an InvalidLimitError."""
        return
