from LoginManager import LoginManager
from StrategiesEnum import Strategies

my_login = LoginManager()
login_strategy = Strategies.EmailLogin
my_login.setStrategy(login_strategy)
my_login.performLogin()