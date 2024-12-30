# crux: a subject has to be notified to multiple objects

from abc import ABC, abstractmethod

class ProductOrder:
    def __init__(self, id) -> None:
        self._id = None
        self.subscribers = list() # "has" abstract Subscribers : Aggregation
        self._status = None 
        # not self.status = None  # This line calls the property setter for status. causes recursion
    
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, new_status):
        self._status = new_status
    
    def register(self, subscriber):
        self.subscribers.append(subscriber)

    def deregister(self, subscriber):
        self.subscribers.remove(subscriber)
 
    def notifySubscribers(self):
        for eachSubscriber in self.subscribers:
            eachSubscriber.update(self._status)

# abstract subscribers
class Subscribers(ABC):
    
    @abstractmethod
    def update(self, *args, **kwargs):
        pass

# concrete subscribers
class Customer(Subscribers):

    def __init__(self, name):
        self.name = name

    def update(self, status):
        print("Product status of customer: ", status)
     

class Seller(Subscribers):

    def __init__(self, name):
        self.name = name

    def update(self, status):
        print("Product status for seller: ", status)


class DeliveryAgent(Subscribers):

    def __init__(self, name):
        self.name = name
    
    def update(self, status):
        print("Product status for DeliveryAgent: ", status)


# main
if __name__ == "__main__":
    status_notifier = ProductOrder(36)
    status_notifier.register(Seller("Retail Company"))
    status_notifier.register(Customer("Dunphy"))
    status_notifier.register(DeliveryAgent("Anna"))

    status_notifier.status = "Item shipped"
    status_notifier.notifySubscribers()
