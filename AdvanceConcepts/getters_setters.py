# LLD/BuilderDesignPattern/Desktop.py

# When you access desktop.motherboard, 
# Python uses the getter method behind the scenes to return the _motherboard value.

# When you assign a value to desktop.motherboard = "Dell Motherboard", 
# Python triggers the setter method and updates the value of _motherboard.



# Getter and setter methods don't have underscores because they are part of the public API of the class
# Getter is expected to return the internal property value. '_status' and not 'status'

    # implcit getter 
    # @property
    # def motherboard(self):
    #     return self._motherboard
    
    # # implicit setter
    # @motherboard.setter
    # def motherboard(self, motherboard):
    #     self._motherboard = motherboard



# Explicitly defining getters and setters
# Here also we dont use underscores to define these methods, because
# it is part of API interface, we are allowing clients to set and get attributes
# without restricting those methods to class itself.
 
# class Desktop:
#     def __init__(self):
#         self.__motherboard = "Intel Z590"

#     def get_motherboard(self):
#         return self.__motherboard

#     def set_motherboard(self, value):
#         self.__motherboard = value

