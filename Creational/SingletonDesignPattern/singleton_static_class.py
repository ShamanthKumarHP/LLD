import threading

# static method
class PaymentGatewayManager:
    _instance = None
    _lock = threading.Lock()  # Mutex to ensure thread safety

    @staticmethod
    def get_instance():
        # Static methods cannot access class-level variables directly
        if PaymentGatewayManager._instance is None:
            with PaymentGatewayManager._lock:
                if PaymentGatewayManager._instance is None:
                    PaymentGatewayManager._instance = PaymentGatewayManager()  # Create instance
        return PaymentGatewayManager._instance

# class method
class PaymentGatewayManager:
    _instance = None
    _lock = threading.Lock()  # Mutex to ensure thread safety

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = cls()  # Create the instance if it doesn't exist
        return cls._instance
