from abc import ABC, abstractmethod

class PaymentFactory(ABC):

    def createCreditCardPayment(self):
        pass

    def createUPIPayment(self):
        pass

    def createNetbankingPayment(self):
        pass

