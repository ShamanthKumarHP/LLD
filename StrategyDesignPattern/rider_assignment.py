# crux: selecting multiple algorithms based on requirement
from abc import ABC, abstractmethod

# Abstract selection algorithm
class Algorithm(ABC):
    @abstractmethod
    def execute(self, amount):
        pass

# concrete classes
class NearestSelect(Algorithm):

    def execute(self, amount):
        print("Selected Rider using Nearest search algorithm for price", amount)


class PocketFriendly(Algorithm):

    def execute(self, amount):
        print("Selected Rider using pocket friendly algorithm for price", amount)


class QuickSelect(Algorithm):
    
    def execute(self, amount):
        print("Selected Rider quick select algorithm for price", amount)


class RiderAssignment:
    def __init__(self):
        self.algorithm = None
    
    def assign_rider(self, amount):
        self.algorithm.execute(amount)
    

if __name__ == "__main__":
    my_rider = RiderAssignment()

    # Select and set the rider assigment strategy at runtime
    assignmet_stategy = PocketFriendly()
    my_rider.algorithm = assignmet_stategy
    my_rider.assign_rider(amount=500)

    assignmet_stategy = QuickSelect()
    my_rider.algorithm = assignmet_stategy
    my_rider.assign_rider(amount=200)
