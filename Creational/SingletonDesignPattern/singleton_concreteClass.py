""" Inheriting singleton design pattern to concrete classes """
import threading

class InternalElevatorStrategy:
    # Singleton implementation at the base class level (if you want to control it for all strategies)
    _instances = {} # Dictionary to store Singleton instances for multiple classes
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances: # we are checking if key is there or not
            with cls._lock:
                if cls not in cls._instances:
                    cls._instances[cls] = super().__new__(cls)
                    print("cls instance", cls._instances)
        return cls._instances[cls]

    def selectNextStop(self):
        raise NotImplementedError("selectNextStop() should be implemented in subclasses")

class ScanAlgo(InternalElevatorStrategy):
    def __init__(self):
        print("init called for scan algo")
        if not hasattr(self, 'initialized'):  # Prevent reinitialization if singleton instance
            self.stops = []
            self.initialized = True

    def selectNextStop(self):
        return self.stops[0] if self.stops else 1

class LookAlgo(InternalElevatorStrategy):
    def __init__(self):
        if not hasattr(self, 'initialized'):  # Prevent reinitialization if singleton instance
            self.stops = []
            self.initialized = True

    def selectNextStop(self):
        return self.stops[-1] if self.stops else 1


scanalgo1 = ScanAlgo()
scanalgo2 = ScanAlgo()
lookAlgo1 = LookAlgo()
print(scanalgo1 == lookAlgo1) # False
# because we are making subclasses as singleton
# In Python, two objects of different classes are considered not equal, regardless of whether they are both Singleton instances.

# If you want ScanAlgo and LookAlgo to be equal based on their internal state (like the stops list), 
# you could override the __eq__ method in both classes:



""" Overiding objects comparision belonging to same base class wrt some attiribute """

class InternalElevatorStrategy:
    _instances = {}

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__new__(cls)
        return cls._instances[cls]

    def __eq__(self, other):
        # Compare instances based on the `stops` list (or any other relevant attribute)
        return isinstance(other, self.__class__) and self.stops == other.stops


class ScanAlgo(InternalElevatorStrategy):
    def __init__(self):
        if not hasattr(self, 'initialized'):
            self.stops = []
            self.initialized = True

class LookAlgo(InternalElevatorStrategy):
    def __init__(self):
        if not hasattr(self, 'initialized'):
            self.stops = []
            self.initialized = True


# Create instances of both classes
scan1 = ScanAlgo()
look1 = LookAlgo()

# Add same stops to both
scan1.stops = [1, 2, 3]
look1.stops = [1, 2, 3]

# Now compare based on internal state (stops)
print(scan1 == look1)  # Output: True (because their 'stops' are equal)


# By default, Python compares objects using identity (whether they are the same object in memory)

# obj1 == obj2  # Calls obj1.__eq__(obj2)
# self: This refers to the current instance of the class 
# other: This refers to the other object being compared 

