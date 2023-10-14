from abc import ABC, abstractmethod

# Interface: PaymentGateway
class PaymentGateway(ABC):
    @abstractmethod
    def processPayment(self, amount: float):
        pass

# Concrete Adapter
class PayPalAdapter(PaymentGateway):
    def __init__(self, paypalAPI):
        self._paypalAPI = paypalAPI
    
    def processPayment(self, amount: float):
        return self._paypalAPI.makePayment(amount)

# Concrete Adapter
class StripeAdapter(PaymentGateway):
    def __init__(self, stripeAPI):
        self._stripeAPI = stripeAPI
    
    def processPayment(self, amount: float):
        return self._stripeAPI.charge(amount)

# Concrete Adapter
class PayTMAdapter(PaymentGateway):
    def __init__(self, paytmAPI):
        self._paytmAPI = paytmAPI
    
    def processPayment(self, amount: float):
        return self._paytmAPI.process_payment(amount)

# Third Party APIs
class PayPal:
    def makePayment(self, amount: float):
        return "PayPal: Payment made for amount: " + str(amount)

class Stripe:
    def charge(self, amount):
        return "Stripe: Payment Charged for amount: " + str(amount)

class PayTM:
    def process_payment(self, amount):
        return "PayTM: Payment processed for amount: " + str(amount)
    

# Client class
class MyPaymentGateway:

    def processPaypalPayment(self):
        paypalPayment = PayPalAdapter( PayPal() )
        return paypalPayment.processPayment(10.50)
    
    def processStripePayment(self):
        stripePayment = StripeAdapter( Stripe() )
        return stripePayment.processPayment(100.0)
    
    def processPaytmPayment(self):
        paytmPayment = PayTMAdapter( PayTM() )
        return paytmPayment.processPayment(25.30)
    

if __name__ == "__main__":

    paymentGateway = MyPaymentGateway()

    paypal = paymentGateway.processPaypalPayment()
    paytm = paymentGateway.processPaytmPayment()
    stripe = paymentGateway.processStripePayment()

    print(paypal)
    print(paytm)
    print(stripe)

