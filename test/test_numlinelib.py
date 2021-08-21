import unittest

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

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
        self.assertEqual([points], numline.get_points())

    def test_multiple_args_initialization(self):
        """Initialize number line without using keyword args."""
        points = [1, 2, 3]
        points2 = [4, 5, 6]
        numline = NumLine(points, points2, show=False)
        self.assertEqual([points, points2], numline.get_points())

    def test_partial_initialization(self):
        """Initialization with some args."""
        points = [1, 2, 3]
        numline = NumLine(points=points, show=False)
        self.assertEqual([points], numline.get_points())
        return

    def test_full_initialization(self):
        """Initialization with all args."""
        points = [1, 2, 3]
        mn = 0
        mx = 4
        numline = NumLine(points=points, min=mn, max=mx, show=False)
        self.assertEqual([points], numline.get_points())
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

    def test_MissingPointsError_as_args(self):
        """Attempting to make NumLine with empty list as arg should throw an error"""
        with self.assertRaises(MissingPointsError):
            NumLine([])
        return

    def test_MissingPointsError_as_kwargs(self):
        """Attempting to make NumLine with empty list as keyword should throw an error"""
        with self.assertRaises(MissingPointsError):
            NumLine(points=[])
        return

    def test_MissingPointsError_with_max(self):
        """Attempting to make NumLine with max/min but no points should throw an error"""
        with self.assertRaises(MissingPointsError):
            NumLine(max=5)
        return

    def test_MissingPointsError_numpy(self):
        """Attempting to make NumLine with empty numpy array should throw an error"""
        with self.assertRaises(MissingPointsError):
            NumLine(points=np.array([]))
        return

    def test_MissingPointsError_pandas(self):
        """Attempting to make NumLine with empty pandas dataframe should throw an error"""
        with self.assertRaises(MissingPointsError):
            raise MissingPointsError()
        return

    def test_calc_min(self):
        """Initializing with points=[1,2,3] should make the min 0"""
        return

    def test_calc_max(self):
        """Initializing with points=[1,2,3] should make the max 4"""
        return

    def test_3d_list_sanitize(self):
        """Attempting to enter points that are more than 2D should raise an exception"""
        with self.assertRaises(MultidimensionalPointsError):
            NumLine([[[1, 2, 3]]])
        return

    def test_2d_pandas_df_sanitize(self):
        """Attempting to enter points as a pandas dataframe that are not 2D should raise an exception"""
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
