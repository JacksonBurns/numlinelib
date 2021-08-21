import matplotlib.pyplot as plt
from numlinelib.exceptions import MissingPointsError


class NumberLine:
    def __init__(self, **kwargs):
        """ """
        self.fig = plt.Figure()
        self._max = None
        self._min = None
        # return the instance of the class
        if not kwargs:
            self._points = []
        # plot points and return the figure
        else:
            # ensure user has provided points
            if kwargs.get("points", False):
                self.set_points(kwargs["points"])
            else:
                raise MissingPointsError("No points provided.")
            self.show()
        return

    def _sanitize_input(self, points):
        """Return a 1D array.

        Args:
            points (iterable): Points to be sanitized.
        """
        # check for pandas, numpy, list, etc. and dimensionality
        return points

    def add_points(self, points):
        """Adds points to the plot.

        Args:
            points (list): Points to be added.
        """
        self._sanitize_input(points)
        self._points.append(points)
        return

    def set_points(self, points):
        """Remove existing points and set new points.

        Args:
            points (list): Points to be added.
        """
        self.clear_points()
        self.add_points(points)
        return

    def clear_points(self):
        """Removes all points on the plot."""
        self._points = []
        # clear points from the number line
        return

    def clear_figure(self):
        """Return to an empty figure."""
        return

    def set_max(self, max):
        return

    def set_min(self, min):
        return

    def set_ticks(self, ticks):
        return

    def get_max(self):
        return

    def set_max(self, max):
        return

    def get_min(self):
        return

    def set_min(self, min):
        return

    def get_lim(self):
        """Returns a tuple of (min, max)

        Returns:
            tuple: Min and max of number line.
        """
        return (self._min, self._max)

    def set_lim(self, mn, mx):
        """Set the minimum and maximum of number line.

        Args:
            mn (number): Minimum.
            mx (number): Maximum.
        """
        self.set_min(mn)
        self.set_max(mx)
        return

    def show(self):
        """Show the number line, return the figure."""
        plt.show()
        return self.fig
