from ElevatorSystem import ElevatorSystem

import ExternalElevatorStrategy 
import InternalElevatorStrategy
from ExternalRequest import ExternalRequest
from InternalRequest import InternalRequest

my_elevator = ElevatorSystem()
my_elevator.total_floors = 10
my_elevator.total_elevators = 6

my_elevator.set_external_request_strategy(ExternalElevatorStrategy.QuickSelect())
my_elevator.set_internal_request_strategy(InternalElevatorStrategy.LookAlgo())
my_elevator.initialise_elevators_system()

extReq = ExternalRequest()
extReq.direction = "UP"
extReq.floor = 7

intReq = InternalRequest()
intReq.elevatorID = 3
intReq.floor = 2

my_elevator.sendExternalRequest(extReq)
my_elevator.sendInternalRequest(intReq)