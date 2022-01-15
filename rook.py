from constants import *
from main import *

class Rook():
    def __init__(self, color):
        self.color = color
        self.type = 'Rook'
        if color == 'B':
            self.image = black_rook
        else:
            self.image = white_rook

    def valid(self, first, second):
        frow, fcol, srow, scol = getrowscols(first, second)

        # check for diagonal
        if first.x != second.x and first.y != second.y:
            return False
        # Check that second tile isn't occupied by own piece
        if isOwnPiece(frow, fcol, srow, scol):
            return False

        xchange, ychange = xychanges(first, second)

        dx, dy = dxdy(xchange, ychange)
        
        frow += dy
        fcol += dx
        while (frow, fcol) != (srow, scol):
            if board.buttons[frow][fcol].isOccupied():
                return False
            frow += dy
            fcol += dx

        return True