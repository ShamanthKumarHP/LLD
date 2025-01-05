from abc import ABC, abstractmethod

# abstract category
class Category(ABC):

    @abstractmethod
    def get_category_name(self):
        pass

#
# Concrete Categories
#
class ModernCategory(Category):

    def get_category_name(self):
        return "Modern"


class TraditionalCategory(Category):

    def get_category_name(self):
        return "Traditional"
    

class VintageCategory(Category):

    def get_category_name(self):
        return "Vintage"
