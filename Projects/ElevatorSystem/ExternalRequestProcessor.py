from ElevatorMgr import ElevatorMgr

class ExternalRequestProcessor:
    def processRequest(self, extReq):
        elevatorMgr = ElevatorMgr.getElevatorMgr()
        elevatorMgr.getElevator(extReq)