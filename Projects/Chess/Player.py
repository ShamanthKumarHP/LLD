class Player:
    def __init__(self):
        self._name = None
        self._status = None
        self._isCurrentPlayer = None
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name
    
    @property
    def status(self):
        return self._status

    @name.setter
    def status(self, name):
        self._status = name
    
    @property
    def isCurrentPlayer(self):
        return self._isCurrentPlayer

    @name.setter
    def isCurrentPlayer(self, isCurrentPlayer):
        self._isCurrentPlayer = isCurrentPlayer