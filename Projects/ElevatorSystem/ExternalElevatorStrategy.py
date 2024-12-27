class ExternalElevatorStrategy:
    def selectElevator(self):
        pass


class NearSelect(ExternalElevatorStrategy):
    def selectElevator(self, floor, direction):
        # can be implemented
        return 2

        
class QuickSelect(ExternalElevatorStrategy):
    def selectElevator(self, floor, direction):
        # can be implemented
        return 1