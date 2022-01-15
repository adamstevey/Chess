from constants import *
from main import *

class Queen():
    def __init__(self, color):
        self.color = color
        self.type = 'Queen'
        if color == 'B':
            self.image = black_queen
        else:
            self.image = white_queen
    
    def valid(self, first, second):
        frow, fcol, srow, scol = getrowscols(first, second)
        # Check is second tile is own piece
        if isOwnPiece(frow, fcol, srow, scol):
            return False
        
        xchange, ychange = xychanges(first, second)

        dx, dy = dxdy(xchange, ychange)

        if (first.x == second.x or first.y == second.y) or (abs(xchange) == abs(ychange)):
            frow += dy
            fcol += dx
            while (frow, fcol) != (srow, scol):
                if board.buttons[frow][fcol].isOccupied():
                    return False
                frow += dy
                fcol += dx
            return True
        return False