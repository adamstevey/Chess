from constants import *
from main import *

class Knight():
    def __init__(self, color):
        self.color = color
        self.type = 'Knight'
        if color == 'B':
            self.image = black_knight
        else:
            self.image = white_knight

    def valid(self, first, second):
        frow, fcol, srow, scol = getrowscols(first, second)

        # check that second tile isn't occupied by own piece
        if isOwnPiece(frow, fcol, srow, scol):
            return False

        # Make sure the move is 'L' shape
        xchange = abs(int(first.x//TILE_WIDTH - second.x//TILE_WIDTH))
        xchange, ychange = xychanges(first, second)
        validSet = [(1, 2), (2, 1)]
        if (abs(xchange), abs(ychange)) in validSet:
            return True
        return False