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


# Concrete Adapter
class XMLtoJSON(TargetAdapter):

    def __init__(self, data):
        self._data = data # has a (in this case composition makes more sense, could be aggregation also)
        self._analyser = JsonAnalytics()
        print("converted data to JSON")
    
    def analyseData(self):
        self._analyser(data)


if __name__ == "__main__":
    data = "JSON DATA"
    analyser = XMLtoJSON(data)
    analyser.analyseData()
