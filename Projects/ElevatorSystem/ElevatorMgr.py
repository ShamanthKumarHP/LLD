import threading
from Elevator import Elevator

class ElevatorMgr:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    @classmethod
    def getElevatorMgr(cls):
        return cls._instance
    
    def __init__(self):
        self.elevators = {}
        self._externalElevatorStrategy = None
        self._internalElevatorStrategy = None
    
    @property
    def externalElevatorStrategy(self):
        return self._externalElevatorStrategy

    @externalElevatorStrategy.setter
    def externalElevatorStrategy(self, extStrategy):
        self._externalElevatorStrategy = extStrategy
    
    @property
    def internalElevatorStrategy(self):
        return self._internalElevatorStrategy
        
    @internalElevatorStrategy.setter
    def internalElevatorStrategy(self, intStrategy):
        self._internalElevatorStrategy = intStrategy
    
    def initialise_elevators(self, num_of_elevator):
        self.elevators = { i : Elevator() for i in range(num_of_elevator) }
        print("elevators", self.elevators)
    
    def getElevator(self, extReq):
        elevatorID = self._externalElevatorStrategy.selectElevator(extReq.floor, extReq.direction)
        self.elevators.get(elevatorID)._ElevatorController.stops.append(extReq.floor)
        print("External Request: Getting Elevator ", elevatorID)

    def addStopToElevator(self, intReq):
        self.elevators.get(intReq.elevatorID)._ElevatorController.stops.append(intReq.floor)
        print(f"InternalRequest: Added stop {intReq.floor} in Elevator {intReq.elevatorID}")

    


