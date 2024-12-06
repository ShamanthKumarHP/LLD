# Sofa - modern, traditional
# Table - modern, traditional

# Problem statement:
# I have modern sofas, modern tables as furnitures

from abc import abstractmethod, ABC

#
# Abstract Products
#
class Sofa(ABC):
    @abstractmethod
    def sitOn(self):
        pass

class Table(ABC):
    @abstractmethod
    def putOn(self):
        pass

# concreate classes represent family of modern products
class ModernSofa(Sofa):
    def sitOn(self):
        print("Sit on modern sofa")

class ModernTable(Table):
    def putOn(self):
        print("Put on modern table")

# concreate classes represent family of traditional products
class TraditionalSofa(Sofa):
    def sitOn(self):
        print("Sit on traditional sofa")
        return super().sitOn()

class TraditionalTable(Table):
    def putOn(self):
        print("Put on Traditional table")
        return super().putOn()

#
# Factory
#

# should we create Table abstract factory and then inside create modern and traditional concreate factories etc
# OR
# should we create Modern abstract factory and then inside create table, sofa etc

# we should ask ourselves, we have set of products, what will customer ask for? 
# ans: He will choose modern or traditional set of products.

# Here its like creating factories of factories

class FurnitureFactory(ABC):
    # this will be exposed to client, client will choose his preference
    def create_furniture(self, furniture_type):
        if furniture_type == "modern":
            return ModernFurnitures()
        elif furniture_type == "traditional":
            return TraditionalFunitures()

class ModernFurnitures(FurnitureFactory):
    def create_sofa(self):
        return ModernSofa()

    def create_table():
        return ModernTable()

class TraditionalFunitures(FurnitureFactory):
    def create_sofa():
        return TraditionalSofa()
    
    def create_table():
        return TraditionalTable()

