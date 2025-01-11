# crux: To have a bridge between refined class and Implementator
# Instead of creating multiple classes with is-a relationship like UberEatsWithGmaps, UberEatsWithAppleMaps, UberRideWithGmaps, UberRideWithAppleMaps,
# Create a bride with has-a relationship by decoupling navigation system

from abc import ABC, abstractmethod


# Abstract Implentator
class NavigationSystem(ABC):
    
    @abstractmethod
    def navigateTo(self):
        pass


class GoogleMaps(NavigationSystem):
    def navigateTo(self):
        print(f"Navigating using {self.__class__.__name__} ")
    

class AppleMaps(NavigationSystem):
    def navigateTo(self):
        print(f"Navigating using {self.__class__.__name__} ")


# Abstract Class
class UberNavigation(ABC):
    def __init__(self):
        self._navigation_system = None # has-a NavigationSystem
    
    @property
    def navigation_system(self):
        return self._navigation_system 

    @navigation_system.setter
    def navigation_system(self, navigation_system):
        self._navigation_system = navigation_system
    
    @abstractmethod
    def navigate(self):
        pass

# Concrete refined class
class UberRide(UberNavigation):
    def __init__(self):
        super().__init__()
        self._driver_name = None
    
    @property
    def driver_name(self):
        return self._driver_name
    
    @driver_name.setter
    def driver_name(self, driver_name):
        self._driver_name = driver_name
    
    def navigate(self, destination):
        print(f"Uber ride with {self._driver_name} to {destination}")
        self.navigation_system.navigateTo()

class uberEats(UberNavigation):
    def __init__(self):
        super().__init__()
        self._restaurant = None
    
    @property
    def restaurant(self):
        return self._restaurant

    @restaurant.setter
    def restaurant(self, restaurant):
        self._restaurant = restaurant
    
    def navigate(self, destination):
        print(f"Uber eats order from {self._restaurant} to {destination}")
        self.navigation_system.navigateTo()

if __name__ == "__main__":
    uber_ride = UberRide()
    maps = GoogleMaps()
    uber_ride.navigation_system = maps
    uber_ride.driver_name = "Ram"
    uber_ride.navigate("HSR")

    uber_eats = uberEats()
    maps = AppleMaps()
    uber_eats.navigation_system = maps
    uber_eats.restaurant = "Meghana Foods"
    uber_eats.navigate("PG")

        

        