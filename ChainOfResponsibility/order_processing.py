# crux: Dynamically selecting next handlers

from abc import ABC, abstractmethod

# abstract class
class Order_Processor(ABC):
    def __init__(self, successHandler=None, failureHandler=None):
        self.successHandler = successHandler
        self.failureHandler = failureHandler
        pass

    @abstractmethod
    def process_order(self):
        pass

# Lets assume there are 4 stages of order processing
# 1. Order Place
# 2. Payment
# 3. Gathering product
# 4. Dispatch

# concrete class
class OrderPlace(Order_Processor): # aggregation + association relationship with abstract class
    def __init__(self, successHandler=None, failureHandler=None):
        super().__init__(successHandler, failureHandler) 
        # association since we are calling super().__init__ 
        # and 
        # aggregation since we have successHandler, failureHandler
    
    def process_order(self):
        status = True
        print("Order placed successfully")
        if status == True:
            self.successHandler.process_order()
        else:
            # self.failureHandler.process_order()
            print("Failed")
    
class Payment(Order_Processor):
    def __init__(self, successHandler=None, failureHandler=None):
        super().__init__(successHandler, failureHandler)
    
    def process_order(self):
        status = True
        print("Payment made successfully")
        if status == True:
            self.successHandler.process_order()
        else:
            # self.failureHandler.process_order()
            print("Failed")


class GatherProduct(Order_Processor):
    def __init__(self, successHandler=None, failureHandler=None):
        super().__init__(successHandler, failureHandler)
    
    def process_order(self):
        status = True
        print("Products gathered successfully")
        if status == True:
            self.successHandler.process_order()
        else:
            # self.failureHandler.process_order()
            print("Failed")

class DispatchOrder(Order_Processor):
    def __init__(self, successHandler=None, failureHandler=None):
        super().__init__(successHandler, failureHandler)
    
    def process_order(self):
        status = True
        print("Order dispatched successfully")
        if status == True:
            # self.successHandler.process_order()
            print("Order Picked up")
        else:
            # self.failureHandler.process_order()
            print("Failed")

if __name__ == "__main__":
    # Create a chain of responsibility for order processing

    # order_process = OrderPlace(Payment(GatherProduct(DispatchOrder())))
    # order_process.process_order()

    # Or we can also set each properties individually
    DispatchOrder_obj = DispatchOrder()
    GatherProduct_obj = GatherProduct(successHandler=DispatchOrder_obj)
    Payment_obj = Payment(successHandler=GatherProduct_obj)
    OrderPlace_obj = OrderPlace(successHandler=Payment_obj)
    OrderPlace_obj.process_order()


