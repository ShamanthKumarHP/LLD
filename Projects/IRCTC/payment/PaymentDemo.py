from PaymentProcessor import PaymentProcessor

my_payment = PaymentProcessor()
my_payment.selectPaymentProvider("Phonepe")
my_payment.initialise_payment()

my_payment.processPaymentWithCreditCard()
my_payment.processPaymentWithNetbanking()
my_payment.processPaymentWithUPI()