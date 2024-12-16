class FoodItem:
    def __init__(self):
        self.__description = None  # Private variable
        self.__price = None  # Private variable

    # Getter for description
    @property
    def description(self):
        return self.__description

    # Setter for description
    @description.setter
    def description(self, value):
        if not value:  # Example validation: description can't be empty
            raise ValueError("Description cannot be empty")
        self.__description = value

    # Getter for price
    @property
    def price(self):
        return self.__price

    # Setter for price
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self.__price = value

class Burger(FoodItem):
    def __init__(self):
        super().__init__()
        self.price = 10
        self.description = "Burger"
        #self.__price = -1 # Direct assignment doesn't work as it is private
        
        # if still Direct assignment made using Name mangling, then it bypasses setter
        #FoodItem.price = -1

# Create an instance of FoodItem
food_item = Burger()
print("food item", food_item.description, food_item.price)