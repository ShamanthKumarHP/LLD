import threading 
from ElevatorMgr import ElevatorMgr
from ExternalRequestProcessor import ExternalRequestProcessor
from InternalRequestProcessor import InternalRequestProcessor

class ElevatorSystem:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance =  super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self, total_floors = None, total_elevators=None):
        self.total_floors = total_floors
        self.total_elevators = total_elevators
        self.elevatorMgr = ElevatorMgr()
    
    def initialise_elevators_system(self):
        self.elevatorMgr.initialise_elevators(self.total_elevators)
        
    
    def set_internal_request_strategy(self, strategy):
        elevatorMgr = ElevatorMgr.getElevatorMgr()
        elevatorMgr.internalElevatorStrategy = strategy
    
    def set_external_request_strategy(self, strategy):
        elevatorMgr = ElevatorMgr.getElevatorMgr()
        elevatorMgr.externalElevatorStrategy = strategy
    
    def sendExternalRequest(self, extReq):
        externalRequestProcessor = ExternalRequestProcessor()
        externalRequestProcessor.processRequest(extReq)

    def sendInternalRequest(self, intReq):
        internalRequestProcessor = InternalRequestProcessor()
        internalRequestProcessor.processRequest(intReq)


    


