from constants import *
from button import Button

class Board():
    def __init__(self):
        self.board = None
        # CREATE BUTTONS
        self.buttons = [
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            []
        ]

        x = 0
        y = 0
        row = 0
        for i in range(NUM_COLS):
            for j in range(NUM_COLS):
                if j == 7:
                    x = 0
                    y += TILE_WIDTH
                    row += 1
                if row < 8:
                    self.buttons[row].append(Button(x, y, TILE_WIDTH, TILE_WIDTH))
                    x += TILE_WIDTH
        self.buttons[0].append(Button(455, 0, TILE_WIDTH, TILE_WIDTH))