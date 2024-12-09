# explain with following steps.


# If we use just __init__, wrong approach
class PaymentGatewayManager:
    _instance = None

    def __init__(self):
        if PaymentGatewayManager._instance is None:
            PaymentGatewayManager._instance = self
            print("Payment Gateway Manager initialized.")
        else:
            print("Payment Gateway Manager already initialized.")

    def process_payment(self, amount: float):
        print(f"Processing payment of ${amount} through the payment gateway.")

# This will fail to ensure a Singleton pattern.
payment_gateway1 = PaymentGatewayManager()
payment_gateway2 = PaymentGatewayManager()
print(payment_gateway1 == payment_gateway2) # these are two different objects

# implementation without thread safe
# ex: Applications with no concurrency requirements.

class PaymentGatewayManager:
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
            print("Payment Gateway Manager initialized.")
        return cls._instance

    def process_payment(self, amount):
        print("processed payment", amount)

# Example usage
if __name__ == "__main__":
    payment_gateway = PaymentGatewayManager()
    payment_gateway.process_payment(100.0)

    # Attempt to create another instance (should return the existing instance)
    another_payment_gateway = PaymentGatewayManager()

    # Check if both instances are the same.
    if payment_gateway is another_payment_gateway:
        print("Both instances are the same. Singleton pattern is working.")
    else:
        print("Singleton pattern is not working correctly.")