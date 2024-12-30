# crux: Doing few additional things before actual things. It's more like a middleware
# Multiple types of proxies are there.

from abc import ABC, abstractmethod

# abstract class
class Image(ABC):
    
    @abstractmethod
    def displayImage(self):
        pass

# concrete real class
class RealImage(Image):

    def __init__(self, name):
        self.name = name
        
    def displayImage(self):
        print("Image Name :", self.name)

# concrete proxy class
class ProxyImage(Image):
    
    def __init__(self, name):
        self.real_image = None
        self.name = name
    
    def displayImage(self):
        if self.real_image == None: # additional check
            self.real_image = RealImage(self.name) # caching => Lazy loading 
        self.real_image.displayImage()

if __name__ == "__main__":
    image = ProxyImage("jpg")

    # some random code

    image.displayImage()

    # image is not loaded again
    image.displayImage()





