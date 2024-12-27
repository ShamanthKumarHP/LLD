# we can either leverage property for getters and setters(Recommended) 
# OR write our own getters and setters
#
class FoodItem:
    def __init__(self):
        print("init of food item")
        self.description = None
        self._price = None # if we are using propery getters and setters then make it protected

    # Getter for description
    def get_description(self):
        return self.description

    # Setter for description
    def set_description(self, value):
        self.description = value

    # Getter for price
    @property
    def price(self):
        return self._price
        #return self.price -> causes recursion

    # Setter for price
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value

class Burger(FoodItem):
    def __init__(self):
        super().__init__()

# Create an instance of FoodItem
food_item = Burger()

# Setting values using setters
food_item.set_description("Burger")
food_item.price = 100

# Getting values using getters
print(food_item.get_description())  # Output: Burger
print(food_item.price)        # Output: 100

# Trying to set an invalid price
try:
    food_item.price = -10 # This will raise an exception
except ValueError as e:
    print(e)  # Output: Price cannot be negative
