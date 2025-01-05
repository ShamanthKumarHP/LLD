from abc import ABC, abstractmethod
from Categories import Category, ModernCategory, VintageCategory, TraditionalCategory
from Furnitures import Furniture, Sofa, Table, Chair


# Abstract Factory Classes
class FurnitureFactory(ABC):
    @abstractmethod
    def create_sofa(self) -> Furniture:
        pass

    @abstractmethod
    def create_table(self) -> Furniture:
        pass


# Concrete Factory Classes
class ModernFurnitureFactory(FurnitureFactory):
    #category: Category

    def __init__(self):
        self.category = ModernCategory()

    def create_sofa(self) -> Furniture:
        return Sofa(self.category)

    def create_table(self) -> Furniture:
        return Table(self.category)
        

class VintageFurnitureFactory(FurnitureFactory):
    def __init__(self):
        self.category = VintageCategory()
    
    def create_sofa(self) -> Furniture:
        return Sofa(self.category)

    def create_table(self) -> Furniture:
        return Table(self.category)


class TraditionalFurnitureFactory(FurnitureFactory):
    def __init__(self):
        self.category = TraditionalCategory()
    
    def create_sofa(self):
        return Sofa(self.category)

    def create_table(self):
        return Table(self.category)

