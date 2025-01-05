from abc import ABC, abstractmethod
from Categories import Category

# abstract furnitue
class Furniture(ABC):

    @abstractmethod
    def display_details(self):
        pass
#
# Concrete Furnitures
#
class Sofa(Furniture):

    def __init__(self, category):
        self.category = category

    def display_details(self):
        print(f"{self.category.get_category_name()} Sofa: For comfort")


class Table(Furniture):
    # Type Annotations:
    category: Category

    def __init__(self, category):
        self.category = category

    def display_details(self):
        print(f"{self.category.get_category_name()} Table: For dinner")


class Chair(Furniture):

    def __init__(self, category: Category):
        self.category = category
    
    def display_details(self):
        print(f"{self.category.get_category_name()} Chair: To sit")
