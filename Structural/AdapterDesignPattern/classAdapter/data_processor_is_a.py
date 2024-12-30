# Not suggested. Also has multiple inheritance - used unlikely
# crux: providing a structure to processing data based on requirement from third party

from abc import ABC, abstractmethod

# Adaptee - let's say third party endpoint

class JsonAnalytics:

    def __init__(self):
        self._data = None
    
    def setData(self, data):
        self._data = data
    
    def analyseData(self):
        if self._data != "JSON DATA":
            print("Data is not in JSON format")
            return
        print("Data received")


# Target Adapter Interface
class TargetAdapter(ABC):

    @abstractmethod
    def analyseData(self):
        return
    
    # def setData(self):
    #     print("testing")


# Concrete Adapter class with Multiple Inheritance
class XMLtoJSON(TargetAdapter, JsonAnalytics):

    def __init__(self, data):
        TargetAdapter.__init__() # (though it's an abstract base class) just for consistency
        JsonAnalytics.__init__()
        self._data = data
        print("converted data to JSON")
        self.setData(self._data) # JsonAnalytics only has setData defined, so it will be called implicitly
    
    def analyseData(self):
        JsonAnalytics.analyseData(self) # As we want JsonAnalytics analyseData function to be called.
        # Note:
        # Here we are telling,
        # Call the analyseData method of the JsonAnalytics class, 
        # but execute it on the current instance (self) of XMLtoJSON
        # As it’s not invoking a static method or a class method.

if __name__ == "__main__":
    data = "JSON DATA"
    analyser = XMLtoJSON(data)
    analyser.analyseData()
