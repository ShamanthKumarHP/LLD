# Building objects with many optional settings.(complex and multpiple configurations)


from abc import ABC, abstractmethod

# abstract product
class Desktop(ABC):
    def __init__(self) -> None:
        self._motherboard = None
        self._processor = None
        self._memory = None
    
    def display(self):
        print("Desktop Specs:")
        print(f"Motherboard: {self._motherboard}")
        print(f"Processor: {self._processor}")
        print(f"Memory: {self._memory}")

    # Refer getters_setters.py

    # implcit getter 
    @property
    def motherboard(self):
        return self._motherboard
    
    # implicit setter
    @motherboard.setter
    def motherboard(self, motherboard):
        self._motherboard = motherboard

    @property
    def processor(self):
        return self._processor
    
    @processor.setter
    def processor(self, processor):
        self._processor = processor

    @property
    def memory(self):
        return self._memory

    @memory.setter
    def memory(self, memory):
        self._memory = memory

# abstract builder
class DesktopBuilder(ABC):

    # DesktopBuilder "has a" Desktop

    # If I have to make it association, then I will pass Desktop as argument and call Desktop methods :)
    # Refer "Desktop_Director & Concrete_Desktop_Builder as Association"

    def __init__(self) -> None:
        self.desktop = Desktop() #  Desktop lifecycle is depends on DesktopBuilder since we are creating it in constructor: Compositon
    
    @abstractmethod
    def build_motherboard(self):
        pass

    @abstractmethod
    def build_processor(self):
        pass

    @abstractmethod
    def build_memory(self):
        pass

    def getDesktop(self):
        return self.desktop


# concreate builders
class Dell_Desktop_Builder(DesktopBuilder):

    def build_motherboard(self):
        self.desktop.motherboard = "Dell motherboard"

    def build_memory(self):
        self.desktop.memory = "8GB"
    
    def build_processor(self):
        self.desktop.processor = "Intel"

class Lenovo_Desktop_Builder(DesktopBuilder):

    def build_motherboard(self):
        self.desktop.motherboard = "Lenovo motherboard"

    def build_memory(self):
        self.desktop.memory = "4GB"
    
    def build_processor(self):
        self.desktop.processor = "Ryzen"

# Builder with chaining
class HP_Desktop_Builder(DesktopBuilder):
    def build_motherboard(self):
        self.desktop.motherboard = "HP motherboard"
        return self
    
    def build_memory(self):
        self.desktop.memory = "32 GB"
        return self

    def build_processor(self):
        self.desktop.processor = "Intel"
        return self
    

# Director - One who actually creates products
# Desktop_Director & Concrete_Desktop_Builder as Association
# class Desktop_Director:
#     def create_desktop(self, builder: DesktopBuilder) -> Desktop: # Desktop_Director is calling Desktop builder's methods -> Assocication
#         builder.build_processor()
#         builder.build_memory()
#         builder.build_motherboard()
#         return builder.getDesktop()

# if __name__ == '__main__':
#     desktop_director = Desktop_Director()

#     lenovo_desktop_builder = Lenovo_Desktop_Builder()
#     lenovo_desktop = desktop_director.create_desktop(lenovo_desktop_builder)
#     lenovo_desktop.display()


# Desktop_Director & Concrete_Desktop_Builder as Composition
# here lifecycle of Concreate Desktop Builder depends on Desktop_Director
# class Desktop_Director:
#     def __init__(self, builder_type):
#         if builder_type == "Dell":
#             self.builder = Dell_Desktop_Builder()
#         elif builder_type == "Lenovo":
#             self.builder = Lenovo_Desktop_Builder()

#     def create_desktop(self) -> Desktop: # Desktop_Director is calling Desktop builder's methods -> Assocication
#         self.builder.build_processor()
#         self.builder.build_memory()
#         self.builder.build_motherboard()
#         return self.builder.getDesktop()

# if __name__ == '__main__':
#     builder_type = "Dell"
#     desktop_director = Desktop_Director(builder_type)
#     my_desktop = desktop_director.create_desktop()
#     my_desktop.display()

# Desktop_Director & Concrete_Desktop_Builder as Aggregation
# where Client creates the concrete product and Desktop_Director has concrete product as property
# If Desktop_Director dies, it will not end life cyle of concrete product as it is created outside.

# class Desktop_Director:
#     def __init__(self, builder_type: DesktopBuilder):
#         self.builder = builder_type # now Desktop_Director has concrete product as property

#     def create_desktop(self) -> Desktop: # Desktop_Director is calling Desktop builder's methods -> Assocication
#         self.builder.build_processor()
#         self.builder.build_memory()
#         self.builder.build_motherboard()
#         return self.builder.getDesktop()

# if __name__ == '__main__':
#     desktop_builder = Dell_Desktop_Builder() # Creating concrete product
#     desktop_director = Desktop_Director(desktop_builder)
#     my_desktop = desktop_director.create_desktop()
#     my_desktop.display()

# Builder with Chaining
class Desktop_Director:
    def create_desktop(self, builder: DesktopBuilder) -> Desktop: # Desktop_Director is calling Desktop builder's methods -> Assocication
        builder.build_processor().build_memory().build_motherboard()
        return builder.getDesktop()

if __name__ == '__main__':
    desktop_builder = HP_Desktop_Builder() # Creating concrete product
    desktop_director = Desktop_Director()
    my_desktop = desktop_director.create_desktop(desktop_builder)
    my_desktop.display()