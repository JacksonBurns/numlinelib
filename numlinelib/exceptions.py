class MissingPointsError(RuntimeError):
    """NumberLine initialized with max/min but not points."""

    def __init__(self, message=None):
        self.message = message
        super().__init__(message)