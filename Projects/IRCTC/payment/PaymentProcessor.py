from PhonepeFactory import PhonepeFactory

class PaymentProcessor:

    def __init__(self):
        self.payment_resolution = None
        self.creditCardPayment = None
        self.upiPayment = None
        self.netbankingPayment = None
    
    def selectPaymentProvider(self, provider):
        if provider == "Phonepe":
            self.payment_resolution = PhonepeFactory()
        elif provider == "Razorpay":
            pass
    
    def initialise_payment(self):
        self.netbanking = self.payment_resolution.createNetbankingPayment()
        self.upi = self.payment_resolution.createUPIPayment()
        self.creditcard = self.payment_resolution.createCreditCardPayment()
    
    def processPaymentWithUPI(self):
        self.upi.processPayment()
    
    def processPaymentWithNetbanking(self):
        self.netbanking.processPayment()
    
    def processPaymentWithCreditCard(self):
        self.creditcard.processPayment()