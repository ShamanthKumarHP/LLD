import threading

"""Creating Only One Instance with respect to base class"""
class InternalElevatorStrategy:
    _instance = None  # Singleton instance for the base class
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        # Check if the instance of the base class already exists
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:  # Double-check inside the lock
                    cls._instance = super().__new__(cls)
                    print("cls instance", cls._instance)
        return cls._instance


class ScanAlgo(InternalElevatorStrategy):
    def __init__(self):
        if not hasattr(self, 'initialized'):  # Prevent reinitialization
            self.stops = []
            self.initialized = True


class LookAlgo(InternalElevatorStrategy):
    def __init__(self):
        if not hasattr(self, 'initialized'):  # Prevent reinitialization
            self.stops = []
            self.initialized = True


# Create instances of both subclasses
scan1 = ScanAlgo()
look1 = LookAlgo()

# Check if both instances are the same
print(scan1 is look1)  # Output: True (both are referring to the same Singleton instance)

# Check if both are referring to the same instance of InternalElevatorStrategy
print(scan1 is InternalElevatorStrategy._instance)  # Output: True
print(look1 is InternalElevatorStrategy._instance)  # Output: True
