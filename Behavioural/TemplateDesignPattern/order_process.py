# crux: Skeleton is defined for what steps to be taken, but behaviour of each step will vary

from abc import ABC, abstractmethod
from typing import final
# abstract class
class OrderProcessTemplate:
    
    @final
    def process_order(self):
        self.verifyOrder()
        self.assignDeliveryPartner()
        self.trackOrder()
    
    @abstractmethod
    def verifyOrder(self):
        pass

    @abstractmethod
    def assignDeliveryPartner(self):
        pass

    @abstractmethod
    def trackOrder(self):
        pass

class LocalOrderProcess(OrderProcessTemplate):
    def verifyOrder(self):
        print("Processing Local order: Order verified")
        return
    
    def assignDeliveryPartner(self):
        print("Processing Local Order: Assigned DP")

    def trackOrder(self):
        print("Processing Local Order: Order Tracking enabled")

class InternationalOrderProcess(OrderProcessTemplate):
    def verifyOrder(self):
        print("Processing International order: Order verified")
        return
    
    def assignDeliveryPartner(self):
        print("Processing International Order: Assigned DP")

    def trackOrder(self):
        print("Processing International Order: Order Tracking enabled")
    

if __name__ == "__main__":
    my_order = LocalOrderProcess()
    my_order.process_order()

    my_order = InternationalOrderProcess()
    my_order.process_order()

        
    
