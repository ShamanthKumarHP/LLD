from ElevatorMgr import ElevatorMgr

class InternalRequestProcessor:
    def processRequest(self, intReq):
        elevatorMgr = ElevatorMgr.getElevatorMgr()
        elevatorMgr.addStopToElevator(intReq)

        