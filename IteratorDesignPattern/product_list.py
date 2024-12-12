from abc import ABC, abstractmethod

# product class
class Product:
    def __init__(self, name = None, price = None):
        self._name = name
        self._price = price
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name
    
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        self._price = price

# abstract Iterator
class Iterator(ABC):

    @abstractmethod
    def hasNext(self):
        pass

    @abstractmethod
    def next(self):
        pass

    @abstractmethod
    def first(self):
        pass

# concrete class
class Product_Iterator(Iterator):

     #_hasNext :bool, _first : Product, _next : Product
    def __init__(self, products):
        self.__current = 0
        self.products = products
    
    def hasNext(self):
        return False if self.__current >= len(self.products) else True
    
    # design the logic we want for next item. 
    def next(self):
        current_product = None
        if self.hasNext():
            current_product = self.products[self.__current]
            self.__current += 1
        return current_product
    
    def first(self):
        current_product = None
        if self.__current == 0:
            current_product = self.products[self.__current]
            self.__current += 1
        return current_product

# aggregate class that provides an iterator
class Inventory:
    def __init__(self):
        self.products = []
    
    def addItem(self, item):
        self.products.append(item)
    
    def createIterator(self):
        return Product_Iterator(self.products)
    

if __name__ == "__main__":
    product1 = Product("Laptop", 99999.99)
    product2 = Product("Smartphone", 49999.99)
    product3 = Product("Headphones", 7999.99)

    inventory_mgr = Inventory()
    inventory_mgr.addItem(product1)
    inventory_mgr.addItem(product2)
    inventory_mgr.addItem(product3)

    iterator = inventory_mgr.createIterator()

    current_product = iterator.first()

    while current_product:
        print(f"name: {current_product.name}, price : {current_product.price}")
        current_product = iterator.next()
