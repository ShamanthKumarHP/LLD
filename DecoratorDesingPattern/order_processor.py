# crux: When we want to dynamically structure the object

# wrapping objects

from abc import ABC, abstractmethod

# Abstract class - representing a food item
class FoodItem:
    def __init__(self):
        self._description = None
        self._price = None

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
        self.price = 100

class Pizza(FoodItem):
    def __init__(self):
        super().__init__()
        self.description = "Pizza"
        self.price = 200

# Why are we inheriting from FoodItem?
# Because, even after adding toppings, it will be stil our food item with just added toppings.
# it will also have description and price
class Decorator(FoodItem):
    def __init__(self, item):
        super().__init__()
        self._food_item = item

    @property
    def food_item(self):
        return self._food_item
    
    @food_item.setter
    def food_item(self, food_item):
        self._food_item = food_item

class ExtraCheeseToppings(Decorator):
    def __init__(self, food_item):
        super().__init__(food_item)
        self.__extraChessPrice = 30
        self.description = self.food_item.description + " with extra cheese"
        self.price = self.food_item.price + self.__extraChessPrice

class ExtraSauceToppings(Decorator):
    def __init__(self, food_item):
        super().__init__(food_item)
        self.__extraSaucePrice = 30
        self.description = self.food_item.description + " with extra sauce"
        self.price = self.food_item.price + self.__extraSaucePrice

if __name__ == "__main__":
    burger = Burger()
    print(burger.description, burger.price)
    
    burger = ExtraSauceToppings(burger)
    print(burger.description, burger.price)
    
    burger = ExtraCheeseToppings(burger)
    print(burger.description, burger.price)

# TODO: How to remove toppings?