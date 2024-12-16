# If we have to use public variables, we can choose to write our own getters and setters
# Internally if we use protected variables and we leverage using "property", although it works same as public.
# but point is to maintain encapsulation 

from abc import ABC, abstractmethod

# Abstract class - representing a food item
class FoodItem:
    def __init__(self):
        # Internally using protected variables
        self._description = None
        self._price = None
    
    # Internally, we are still using protected variables (e.g., _description, _price) 
    # to store the data, but we expose them as public attributes through the property mechanism.
    @property
    def description(self):
        return self._description
    
    @description.setter
    def description(self, description):
        self._description = description
    
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value

class Burger(FoodItem):
    def __init__(self):
        super().__init__()
        self.description = "Burger"
        self.price = -1
        #self._price = -1 # Direct assignment bypasses the property setter

if __name__ == "__main__":
    burger = Burger()
    print(burger.price)
    