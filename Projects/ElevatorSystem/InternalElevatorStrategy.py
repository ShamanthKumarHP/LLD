class InternalElevatorStrategy:
    def selectNextStop(self):
        pass

class ScanAlgo(InternalElevatorStrategy):
    def __init__(self):
        self.stops = []

    def selectNextStop(self):
        return self.stops[0] if self.stops else 1

class LookAlgo(InternalElevatorStrategy):
    def __init__(self):
        self.stops = []

    def selectNextStop(self):
        return self.stops[0] if self.stops else 1

