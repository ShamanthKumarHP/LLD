import LoginStrategy
from StrategiesEnum import Strategies

class LoginManager:
    def __init__(self):
        self.strategy = None
    
    def setStrategy(self, strategy_val):
        if strategy_val ==  Strategies.EmailLogin:
            self.strategy = LoginStrategy.EmailLogin()
        elif strategy_val == Strategies.PasswordLogin:
            self.strategy = LoginStrategy.PasswordLogin()
        elif strategy_val == Strategies.ThirdPartyLogin:
            self.strategy = LoginStrategy.ThirdPartyLogin()
    
    def performLogin(self):
        self.strategy.login()
    