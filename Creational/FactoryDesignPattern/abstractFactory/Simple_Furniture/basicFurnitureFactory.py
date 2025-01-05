# crux: creating families of similar objects

# Sofa - modern, traditional
# Table - modern, traditional

# Problem statement:
# I have few furnitures and have variations of categories modern sofas, modern tables as furnitures
# would like to more categories in future, like vintage etc

from abc import abstractmethod, ABC

# class Furniture: If more abstraction needed

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
# Refer notes.txt

# Here its like creating factories of factories

# Abstract Factory Class
class FurnitureFactory(ABC):
    @abstractmethod
    def create_sofa(self) -> Sofa: # less abstraction, if had Furniture class then more abstraction
        pass
    
    @abstractmethod
    def create_table(self) -> Table:
        pass


class ModernFurnituresFactory(FurnitureFactory):
    def create_sofa(self):
        return ModernSofa()

    def create_table():
        return ModernTable()

class TraditionalFunituresFactory(FurnitureFactory):
    def create_sofa():
        return TraditionalSofa()
    
    def create_table():
        return TraditionalTable()


 # this will be exposed to client, client will choose his preference
class FurnitureClient(ABC):
   
    def create_furniture(self, furniture_type: str):
        if furniture_type == "modern":
            return ModernFurnituresFactory()
        elif furniture_type == "traditional":
            return TraditionalFunituresFactory()