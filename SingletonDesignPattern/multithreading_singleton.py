# Refer GIL

# implementation with thread safe
# ex: Application with multithreading
import threading
class PaymentGatewayManager:
    _instance = None
    _lock = threading.Lock() # mutex

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            with cls._lock: # this will manage acquiring and releasing lock
                if cls._instance is None:
                    cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self, value=None):
        if not hasattr(self, 'initialized'):  # Prevent reinitialization
            self.value = value
            self.initialized = True

# Directly create the Singleton object
singleton1 = PaymentGatewayManager()
print(singleton1)

# Attempting to create another instance will return the same object
singleton2 = PaymentGatewayManager()
print(singleton2)

# Checking if both instances are the same
print(singleton1 is singleton2)  # This will print: True

if __name__ == "__main__":

    thread1 = threading.Thread(target=PaymentGatewayManager())
    thread2 = threading.Thread(target=PaymentGatewayManager())

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()