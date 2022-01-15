from constants import *
from main import *

class Bishop():
    def __init__(self, color):
        self.color = color
        self.type = 'Bishop'
        if color == 'B':
            self.image = black_bishop
        else:
            self.image = white_bishop

    def valid(self, first, second):
        frow, fcol, srow, scol = getrowscols(first, second)
        if isOwnPiece(frow, fcol, srow, scol):
            return False
        
        # find change in x and y between first and second tiles
        xchange, ychange = xychanges(first, second)

        # check that move is diagonal
        if abs(ychange) == abs(xchange):

            # Check for pieces in between
            dx, dy = dxdy(xchange, ychange)
            frow += dy
            fcol += dx
            while frow != srow:
                if board.buttons[frow][fcol].isOccupied():
                    return False
                frow += dy
                fcol += dx
            return True

        return False