import matplotlib.pyplot as plt


class NumberLine:
    def __init__(self, *args):

        self.fig = plt.Figure()
        # return the instance of the class
        if not args:
            self.points = []
        # plot points and return the figure
        else:
            self.set_points(args)
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
        self.points.append(points)
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
        self.points = []
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

    def show(self):
        """Show the number line, return the figure."""
        plt.show()
        return self.fig
