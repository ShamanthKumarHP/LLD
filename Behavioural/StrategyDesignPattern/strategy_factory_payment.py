# Here, we will delegate creation of algorithms to Factory
# and Strategy will be used for just execution

from abc import ABC, abstractmethod

# Abstract Payment Strategy
class PaymentStrategy(ABC):
    
    @abstractmethod
    def process_payemnt(self):
        pass

# Concrete Payment Classes
class PayPal(PaymentStrategy):
    def process_payemnt(self, amount):
        print("Processed payment using PayPal", amount)

class RuPay(PaymentStrategy):
    def process_payemnt(self, amount):
        print("Processed Payment using RuPay", amount)

class CreditCard(PaymentStrategy):
    def process_payemnt(self, amount):
        print("Processed payment using credit card", amount)

class UPI(PaymentStrategy):
    def process_payemnt(self, amount):
        print("Processed payment using UPI", amount)


# Simple Factory
class PaymentFactory:
    def get_payment_strategy(strategy):
        if strategy == "creditcard":
            return CreditCard()
        elif strategy == "paypal":
            return PayPal()
        elif strategy == "upi":
            return UPI()
        else:
            return RuPay() 

class PaymentProcessor:
    def __init__(self):
        self.strategy = None
        pass

    def setPaymentStrategy(self, payment_strategy):
        self.strategy = PaymentFactory.get_payment_strategy(payment_strategy)
    
    def processPayment(self, amount):
        self.strategy.process_payemnt(amount)

    def __del__(self):
        print("clearing strategy")
        self.strategy = None

if __name__ == "__main__":
    payment_processor = PaymentProcessor()
    payment_processor.setPaymentStrategy("creditcard")
    payment_processor.processPayment(amount=100)
    #del payment_processor
    payment_processor = PaymentProcessor()
    payment_processor.setPaymentStrategy("upi")
    payment_processor.processPayment(amount = 100)



    



 