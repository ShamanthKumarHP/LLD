# 
# products
#
from abc import abstractmethod, ABC # abstract base class
class ILogger(ABC):
    @abstractmethod
    def log(self, *args, **kwargs):
        pass

class ErrorLogger(ILogger):
    def log(self, message):
        print("Error logger:", message)
    
class InfoLogger(ILogger):
    def log(self, message):
        print("Info logger: ", message)

class WarnLogger(ILogger):
    def loge(self, message):
        print("Warn logger", message)



#
# Factory
#

class Abstract_Factory_Logger(ABC):
    @abstractmethod
    def create_logger(self):
        pass

# Concrete Factory Loggers
class Factory_WarnLogger(Abstract_Factory_Logger):
    def create_logger(self):
        return WarnLogger()

class Factory_InfoLogger(Abstract_Factory_Logger):
    def create_logger(self):
        return InfoLogger()

class Factory_ErrorLogger(Abstract_Factory_Logger):
    def create_logger(self):
        return ErrorLogger()
    
#
# client
#

class Client():
    def get_logger(self):
        warn_factory = Factory_WarnLogger()
        error_factory = Factory_ErrorLogger()
        info_factory = Factory_InfoLogger()

        warn_logger = warn_factory.create_logger()
        warn_logger.log(message="executed by factory")

if __name__ == '__main__':
    obj = Client()
    obj.get_logger()
