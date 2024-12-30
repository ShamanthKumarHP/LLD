# crux: similar objects creation by encapsulate creation process

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
    def log(self, message):
        print("Warn logger", message)

#
# factory (simple factory)
#
class LoggerFactory():
    @staticmethod
    def createLogger(logger_type):
        if logger_type == "warn":
            return WarnLogger()
        elif logger_type == "info":
            return InfoLogger()
        elif logger_type == "error":
            return ErrorLogger()

# Problem is, its not extensible. 
# if i get one more logger type, again i will have to touch {if else block} which disturbs others.
# so have a abstract factory, and then create concrete factory.

#
# client
#

class Client():
    def get_logger(self):
        logger_type = "warn"
        logger = LoggerFactory.createLogger(logger_type)
        logger.log(message="executed by factory")

if __name__ == '__main__':
    obj = Client()
    obj.get_logger()

        
