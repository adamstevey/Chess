from constants import *
from main import *

class Pawn():
    def __init__(self, color):
        self.color = color
        self.type = 'Pawn'
        self.hasmoved = False
        if color == 'B':
            self.image = black_pawn
        else:
            self.image = white_pawn
    
    def valid(self, first, second, turn):
        # Check that move is forward 1 or 2 squares and whether or not piece has moved
            global validTest
            if turn == 'B' and not self.hasmoved:
                validSet = [-1, -2]
            elif turn == 'B' and self.hasmoved:
                validSet = [-1]
            elif turn == 'W' and not self.hasmoved:
                validSet = [1, 2]
            else:
                validSet = [1]
            if (first.y // TILE_WIDTH) - (second.y // TILE_WIDTH) in validSet:

                # If move is not diagonal
                if second.x == first.x:
                    if not second.isOccupied():
                        srow = int(second.y // TILE_WIDTH)
                        col = int(second.x // TILE_WIDTH)
                        frow = int(first.y // TILE_WIDTH)

                        # For white pawns
                        if turn == 'W':
                            while srow < frow:
                                if board.buttons[srow][col].isOccupied():
                                    return False
                                srow += 1
                            if not validTest:
                                self.hasmoved = True
                            return True
                        
                        # For black pawns
                        else:
                            while srow > frow:
                                if board.buttons[srow][col].isOccupied():
                                    return False
                                srow -= 1
                            if not validTest:
                                self.hasmoved = True
                            return True

                # If move is diagonal
                else:
                    if abs((first.y // TILE_WIDTH) - (second.y // TILE_WIDTH)) == 1:
                        if abs((first.x // TILE_WIDTH) - (second.x // TILE_WIDTH)) == 1:
                            row = int(second.y // TILE_WIDTH)
                            col = int(second.x // TILE_WIDTH)    
                            if board.buttons[row][col].isOccupied() and board.board[row][col].color != turn:
                                self.hasmoved = True
                                return True

            return False