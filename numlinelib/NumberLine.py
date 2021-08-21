import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from numlinelib.exceptions import (
    MissingPointsError,
    MultidimensionalPointsError,
    InvalidLimitError,
)


class NumberLine:
    def __init__(self, *args, **kwargs):
        """Expects points (keyword optional), max, min, ticks, show (bool), marker, color, size, labels, xlabel, title"""
        self.fig = plt.figure(figsize=(6, 1))
        self._max = None
        self._min = None
        self._ticks = None
        self._points = None
        self._labels = None
        # return the instance of the class
        if not kwargs and not args:
            return
        # plot points and return the figure
        else:
            # ensure user has provided points
            if args:
                self.set_points(args)
            elif type(kwargs.get("points", 0)) == np.ndarray:
                if kwargs.get("points").size > 0:
                    self.set_points(kwargs["points"])
                else:
                    raise MissingPointsError("No points provided.")
            elif kwargs.get("points", False):
                self.set_points(kwargs["points"])
            else:
                raise MissingPointsError("No points provided.")
            # set the max and min or calculate them
            if kwargs.get("max", False):
                self.set_max(kwargs["max"])
            else:
                self.set_max(self._calc_max())
            if kwargs.get("min", False):
                self.set_max(kwargs["min"])
            else:
                self.set_min(self._calc_min())
            # set the ticks if provided, else leave as auto
            if kwargs.get("ticks", False):
                self._ticks = self.set_ticks(kwargs["ticks"])
            else:
                self._ticks = "auto"
            self._labels = kwargs.get("labels", [])
            # do not show plot if indicated
            if kwargs.get("show", True):
                self.show(
                    marker=kwargs.get("marker", "."),
                    color=kwargs.get("color", "g"),
                    s=kwargs.get("size", 400),
                    xlabel=kwargs.get("xlabel", ""),
                    title=kwargs.get("title", ""),
                )
            else:
                return
        return

    def _calc_min(self):
        """Subtract 1 from min of points for min.

        Returns:
            number: Minimum of points minus 1.
        """
        return np.min(self.get_points()) - 1

    def _calc_max(self):
        """Add 1 to max of points for max.

        Returns:
            number: Maximum of points plus 1.
        """
        return np.max(self.get_points()) + 1

    def _sanitize_input(self, points):
        """Return a nested list with equal length elements.

        Args:
            points (iterable): Points to be sanitized.
        """
        # convert args input to a nested list
        if type(points) == tuple:
            points = list(points)
        # converty numpy to a list
        if type(points) == np.ndarray:
            new_list = points.tolist()
        # convert pandas to a list
        elif type(points) == pd.DataFrame:
            new_list = points.values.tolist()
        else:
            new_list = points
        # empty list
        if len(new_list) == 0:
            raise MissingPointsError("No points provided (points={}).".format(points))
        # not a list of ints or floats
        if type(new_list[0]) == list:
            try:
                new_list[0][0][0]
                raise MultidimensionalPointsError(
                    "Input points are not one- or two-dimensional."
                )
            except IndexError:
                raise MissingPointsError(
                    "No points provided in inner group (points={}).".format(points)
                )
            except TypeError:
                pass
        # catch one dimensional lists
        if type(new_list[0]) != list:
            new_list = [new_list]
        return new_list

    def add_points(self, points, label=None):
        """Adds points to the plot.

        Args:
            points (list): Points to be added.
        """
        new_list = self._sanitize_input(points)
        self._points.extend(new_list)
        if label is not None:
            self._labels.extend(label)
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
        self.fig.clf()
        return

    def clear_all(self):
        """Reset all values to defaults."""
        self.clear_points()
        self.clear_figure()
        self._min = None
        self._max = None
        self._labels = None
        self._ticks = None
        return

    def get_labels(self):
        """Return the current labels if set, else None.

        Returns:
            list: List of strings.
        """
        return self._labels

    def set_max(self, mx):
        """Set the maximum for the number line.

        Args:
            mx (number): Maximum for the number line.

        Raises:
            InvalidLimitError: Raised when maximum is less than the minimum.
        """
        if self.get_min() is None or mx > self.get_min():
            self._max = mx
        else:
            raise InvalidLimitError(
                "Maximum ({}) must be larger than minimum ({})".format(
                    mx, self.get_min()
                )
            )
        return

    def set_min(self, mn):
        """Set the minimum for the number line.

        Args:
            mn (number): Minimum for the number line.

        Raises:
            InvalidLimitError: Raised when minimum is more than the maximum.
        """
        if self.get_max() is None or mn < self.get_max():
            self._min = mn
        else:
            raise InvalidLimitError(
                "Minimum ({}) must be less than maximum ({})".format(mn, self.get_max())
            )
        return

    def set_ticks(self, ticks):
        """Sets the ticks for the number line.

        Args:
            ticks (list): Ticks for the number line.

        Raises:
            InvalidLimitError: Raised when max of ticks is larger than max of number line.
            InvalidLimitError: Raised when min of ticks is less than the min of number line.
        """
        new_ticks = self._sanitize_input(ticks)
        if self.get_min() is not None and min(new_ticks) < self.get_min():
            raise InvalidLimitError(
                "Minimum of ticks ({}) is less than minimum of number line ({})".format(
                    min(new_ticks), self.get_min()
                )
            )
        if self.get_max() is not None and max(new_ticks) > self.get_max():
            raise InvalidLimitError(
                "Maximum of ticks ({}) is greater than maximum of number line ({})".format(
                    max(new_ticks), self.get_max()
                )
            )
        self._ticks = new_ticks
        return

    def get_ticks(self):
        """Return the current ticks.

        Returns:
            list: Current ticks for number line.
        """
        return self._ticks

    def get_max(self):
        """Return the current maximum of the number line.

        Returns:
            number: Maximum of number line.
        """
        return self._max

    def get_min(self):
        """Return the current minimum of the number line.

        Returns:
            number: Minimum of the number line.
        """
        return self._min

    def get_points(self):
        """Return the current points.

        Returns:
            list: points currently on the number line.
        """
        return self._points

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

    def show(self, **kwargs):
        """Show the number line, return the figure."""
        # plot the data horizontally
        if len(self.get_points()) == 1:
            plot = plt.scatter(
                self.get_points(),
                [0 for _ in self.get_points()],
                zorder=10,
                clip_on=False,
                marker=kwargs.get("marker", "."),
                color=kwargs.get("color", "g"),
                edgecolors="k",
                s=kwargs.get("s", 400),
            )
        else:
            for idx, pnts in zip(range(len(self.get_points())), self.get_points()):
                plot = plt.scatter(
                    pnts,
                    [0 for _ in pnts],
                    zorder=10,
                    clip_on=False,
                    marker=kwargs.get("marker", "."),
                    color=kwargs.get("color", "auto")[idx],
                    label=self.get_labels()[idx],
                    edgecolors="k",
                    s=kwargs.get("s", 400),
                )
        # set the limits
        plt.xlim(self.get_min(), self.get_max())
        plt.ylim(0, 1)
        # set the horizontal ticks
        if self._ticks == "auto":
            pass
        else:
            plt.xticks(self.get_ticks())
        # turn off the vertical axis
        ax = plt.gca()
        ax.spines["left"].set_visible(False)
        ax.axes.get_yaxis().set_visible(False)
        # turn off the box
        ax.spines["right"].set_visible(False)
        ax.spines["top"].set_visible(False)
        # move plot up
        plt.gcf().axes[0].set_position([0.1, 0.5, 0.8, 0])
        # add the text
        plt.title(kwargs.get("title", "") + "\n")
        plt.xlabel(kwargs.get("xlabel", ""))
        plt.show()
        return self.fig
