from constants import *
from main import *

class King():
    def __init__(self, color):
        self.color = color
        self.type = 'King'
        if color == 'B':
            self.image = black_king
        else:
            self.image = white_king

    def valid(self, first, second):
        frow, fcol, srow, scol = getrowscols(first, second)
        # Check that second tile is not occupied by own
        if isOwnPiece(frow, fcol, srow, scol):
            return False
        xchange, ychange = xychanges(first, second)

        if abs(xchange) > 1 or abs(ychange) > 1:
            return False
        return True