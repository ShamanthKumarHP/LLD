import InternalElevatorStrategy 

class ElevatorController:
    def __init__(self):
        self.stops = []
        self.nextStop = None

    def addStop(self, floor):
        self.stops.append(floor)
    
    def moveToNextStop(self):
        strategy = InternalElevatorStrategy.LookAlgo()
        nextStop  = strategy.selectNextStop()
        self.stops.append(nextStop)
    
