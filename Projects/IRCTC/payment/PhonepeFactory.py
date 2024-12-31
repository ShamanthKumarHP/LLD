from PaymentFactory import PaymentFactory

from PhonepeCCPayment import PhonepeCCPayment
from PhonepeNetbanking import PhonepeNetbanking
from PhonepeUPI import PhonepeUPIPayment

class PhonepeFactory(PaymentFactory):
    def createCreditCardPayment(self):
        return PhonepeCCPayment()
    
    def createNetbankingPayment(self):
        return PhonepeNetbanking()
    
    def createUPIPayment(self):
        return PhonepeUPIPayment()