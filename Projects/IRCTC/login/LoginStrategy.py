from abc import ABC, abstractmethod
Strategies = {}
class LoginStrategy(ABC):

    @abstractmethod
    def getName(self):
        pass

    @abstractmethod
    def login(self):
        pass

class EmailLogin(LoginStrategy):

    def __init__(self):
        self._name = None
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name
    
    def getName(self):
        return self.name
    
    def login(self):
        # TODO
        print("Email login")
        return True


class ThirdPartyLogin(LoginStrategy):

    def __init__(self):
        self._name = None
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name
    
    def getName(self):
        return self.name
    
    def login(self):
        # TODO
        print("ThirdParty login")
        return True
    

class PasswordLogin(LoginStrategy):

    def __init__(self):
        self._name = None
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name
    
    def getName(self):
        return self.name
    
    def login(self):
        # TODO
        print("Password login")
        return True