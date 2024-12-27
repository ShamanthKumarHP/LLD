from ElevatorController import ElevatorController
class Elevator:
    def __init__(self):
        self._id = None
        self._status = None
        self._currFloor = None
        self._currDirection = None
        self._ElevatorController = ElevatorController()
    
    @property
    def ElevatorController(self):
        return self.ElevatorController
