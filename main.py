import pygame
import os

from constants import *
from king import King
from queen import Queen
from bishop import Bishop
from knight import Knight
from rook import Rook
from pawn import Pawn
from board import Board

pygame.init()

# OBJECTS
board = Board()

# FUNCTIONS
def showValid():
    global TILE_SELECTED, FIRST_TILE, turn, validTest
    if TILE_SELECTED:
        x = int(FIRST_TILE.x // TILE_WIDTH)
        y = int(FIRST_TILE.y // TILE_WIDTH)
        if pos[1]//TILE_WIDTH < 8:
            HOVER_TILE = board.buttons[int(pos[1]//TILE_WIDTH)][int(pos[0]//TILE_WIDTH)]
            validTest = True
            if board.board[y][x].type == 'Pawn':
                if board.board[y][x].valid(FIRST_TILE, HOVER_TILE, turn):
                    pygame.draw.circle(WIN, HOVER_COLOR, (HOVER_TILE.x + TILE_WIDTH/2, HOVER_TILE.y + TILE_WIDTH/2), 10)
            else:
                if board.board[y][x].valid(FIRST_TILE, HOVER_TILE):
                    pygame.draw.circle(WIN, HOVER_COLOR, (HOVER_TILE.x + TILE_WIDTH/2, HOVER_TILE.y + TILE_WIDTH/2), 10)
            validTest = False

def dxdy(xchange, ychange):
    if xchange != 0 :
            dx = xchange // abs(xchange)
    else:
        dx = 0
    if ychange != 0:
        dy = ychange // abs(ychange)
    else:
        dy = 0
    return dx, dy

def xychanges(first, second):
    xchange = int(second.x//TILE_WIDTH - first.x//TILE_WIDTH)
    ychange = int(second.y//TILE_WIDTH - first.y//TILE_WIDTH)
    return xchange, ychange

def isOwnPiece(frow, fcol, srow, scol):
    if board.buttons[srow][scol].isOccupied():
        if board.board[srow][scol].color == board.board[frow][fcol].color:
            return True
    return False

def getrowscols(first, second):
    frow = int(first.y // TILE_WIDTH)
    fcol = int(first.x // TILE_WIDTH)
    srow = int(second.y // TILE_WIDTH)
    scol = int(second.x // TILE_WIDTH)
    return  frow, fcol, srow, scol

def move_is_valid():
    global FIRST_TILE, SECOND_TILE, turn
    col = int(FIRST_TILE.x // TILE_WIDTH)
    row = int(FIRST_TILE.y // TILE_WIDTH)
    piece = board.board[row][col]
    if piece.type == 'Pawn':
        if piece.valid(FIRST_TILE, SECOND_TILE, turn):
            return True
        else:
            SECOND_TILE = None
    else:
        if piece.valid(FIRST_TILE, SECOND_TILE):
            return True
        else:
            SECOND_TILE = None

def move_piece():
    global FIRST_TILE, SECOND_TILE, turn
    if move_is_valid():
        col = int(FIRST_TILE.x // TILE_WIDTH)
        row = int(FIRST_TILE.y // TILE_WIDTH)
        piece = board.board[row][col]
        x = int(SECOND_TILE.x // TILE_WIDTH)
        y = int(SECOND_TILE.y // TILE_WIDTH)
        board.board[y][x] = piece
        board.board[row][col] = 0
        SECOND_TILE = None
        if turn == 'W':
            turn = 'B'
        else:
            turn = 'W'
        pass

def pieceIsSelected():
    for row in board.buttons:
        for tile in row:
            if tile != 0:
                if tile.selected:
                    return True
    return False


TILE_SELECTED = False
FIRST_TILE = None
SECOND_TILE = None

def handle_button_clicks(event, pos):
    global TILE_SELECTED, SECOND_TILE, FIRST_TILE, turn
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button:
            col = int(pos[0] // TILE_WIDTH)
            row = int(pos[1] // TILE_WIDTH)

            # If click is below board
            if row >= 8:
                return

            # Deselect Piece
            if board.buttons[row][col].selected:
                board.buttons[row][col].selected = False
                TILE_SELECTED = False
                SECOND_TILE = None
            else:
                # Handle Second Click
                if TILE_SELECTED:
                    for x in range(NUM_COLS):
                        for y in range(NUM_COLS):
                            if board.buttons[x][y].selected:
                                board.buttons[x][y].selected = False
                    SECOND_TILE = board.buttons[row][col]
                    TILE_SELECTED = False

                # Handle First Click
                else:
                    if board.buttons[row][col].isOccupied() and board.board[row][col].color == turn:
                        board.buttons[row][col].selected = True
                        TILE_SELECTED = True
                        FIRST_TILE = board.buttons[row][col]

def draw_pieces():
    for row in range(len(board.board)):
        for col in range(len(board.board)):
            if board.buttons[row][col].selected:
                pygame.draw.rect(WIN, SELECTED_COLOR, (board.buttons[row][col].x, board.buttons[row][col].y, TILE_WIDTH, TILE_WIDTH))
                pygame.draw.rect(WIN, HOVER_COLOR, (board.buttons[row][col].x + SELECTED_PADDING, board.buttons[row][col].y + SELECTED_PADDING
                , TILE_WIDTH - (2*SELECTED_PADDING), TILE_WIDTH - (2*SELECTED_PADDING)))
            if board.board[row][col] != 0:
                WIN.blit(board.board[row][col].image, (col* TILE_WIDTH, row*TILE_WIDTH))

def set_board():
    board.board = [
        [Rook('B'), Knight('B'), Bishop('B'), Queen('B'), King('B'), Bishop('B'), Knight('B'), Rook('B')], 
        [Pawn('B'), Pawn('B'), Pawn('B'), Pawn('B'), Pawn('B'), Pawn('B'), Pawn('B'), Pawn('B')], 
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [Pawn('W'), Pawn('W'), Pawn('W'), Pawn('W'), Pawn('W'), Pawn('W'), Pawn('W'), Pawn('W')],
        [Rook('W'), Knight('W'), Bishop('W'), Queen('W'), King('W'), Bishop('W'), Knight('W'), Rook('W')]
        ]

def handle_buttons(pos):
    global turn
    for row in range(len(board.buttons)):
        for col in range(len(board.buttons)):
            if board.buttons[row][col].isOver(pos) and board.buttons[row][col].isOccupied() and not TILE_SELECTED and turn == board.board[row][col].color:
                pygame.draw.rect(WIN, HOVER_COLOR, (board.buttons[row][col].x, board.buttons[row][col].y, TILE_WIDTH, TILE_WIDTH))

def draw_grid():
    x = 0
    y = 0
    checker = 1
    for i in range(NUM_COLS):
        for j in range(NUM_COLS):
            if checker==1:
                pygame.draw.rect(WIN, DARK_BEIGE, (x, y, TILE_WIDTH, TILE_WIDTH))
            else:
                pygame.draw.rect(WIN, BEIGE, (x, y, TILE_WIDTH, TILE_WIDTH))
            if j != 7:
                checker*= -1
            x += TILE_WIDTH
        x = 0
        y += TILE_WIDTH

def create_win():
    return pygame.display.set_mode((WIDTH, HEIGHT))

def draw_back(WIN, pos):
    global turn
    if turn == 'W':
        WIN.fill(WHITE)
    else:
        WIN.fill(BLACK)
    draw_grid()
    handle_buttons(pos)
    draw_pieces()
    showValid()
    
    pygame.display.update()

# MAIN LOOP
run = True
WIN = create_win()
set_board()
turn = 'W'

while run:
    pos = pygame.mouse.get_pos()
    draw_back(WIN, pos)
    
    for event in pygame.event.get():
        handle_button_clicks(event, pos)
        if event.type == pygame.QUIT:
            run = False
    if SECOND_TILE != None:
        move_piece()

pygame.quit()