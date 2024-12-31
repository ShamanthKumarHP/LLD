from abc import abstractmethod, ABC

class Pawn(ABC):
    def __init__(self):
        self._name = None
        self._isWhite = None
        self._isKilled = None

    @abstractmethod
    def canMove(self):
        pass

    @abstractmethod
    def move(self):
        pass

class Soldier(Pawn):
    def __init__(self):
        super().__init__()
        self._name = "Soldier"
        self._isWhite = True
        self._isKilled = False


class King(Pawn):
    def __init__(self):
        super().__init__()
        self._name = "King"
        self._isWhite = True
        self._isKilled = False


class Queen(Pawn):
    def __init__(self):
        super().__init__()
        self._name = "Queen"
        self._isWhite = True
        self._isKilled = False


class Bishop(Pawn):
    def __init__(self):
        super().__init__()
        self._name = "Bishop"
        self._isWhite = True
        self._isKilled = False


class Knight(Pawn):
    def __init__(self):
        super().__init__()
        self._name = "Knight"
        self._isWhite = True
        self._isKilled = False


class Rook(Pawn):
    def __init__(self):
        super().__init__()
        self._name = "Rook"
        self._isWhite = True
        self._isKilled = False

