from constants import *
from main import *

class Button():
    def __str__(self):
        return f"Button {self.x}, {self.y}"

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.selected = False
    
    def isOver(self, pos):
        if pos[0] > self.x and pos[0] < self.x+self.width:
            if pos[1] > self.y and pos[1] < self.y+self.height:
                return True
        return False

    def isOccupied(self):
        col = int(self.x//TILE_WIDTH)
        row = int(self.y//TILE_WIDTH)
        if board.board[row][col] != 0:
            return True
        return False