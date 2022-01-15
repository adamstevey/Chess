import pygame
import os

# CONSTANTS
WIDTH, HEIGHT = (520, 600)
NUM_COLS = 8
TILE_WIDTH = WIDTH/NUM_COLS
SELECTED_PADDING = 3

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (255, 0, 255)
BEIGE = (200, 120, 65)
DARK_BEIGE = (180, 100, 50)
HOVER_COLOR = (0, 180, 255) 
SELECTED_COLOR = (0, 255, 255)

# IMAGES
black_pawn = pygame.image.load(os.path.join('Chess Pieces', 'Pawn B.png'))
white_pawn = pygame.image.load(os.path.join('Chess Pieces', 'Pawn W.png'))
black_king = pygame.image.load(os.path.join('Chess Pieces', 'King B.png'))
white_king = pygame.image.load(os.path.join('Chess Pieces', 'King W.png'))
black_knight = pygame.image.load(os.path.join('Chess Pieces', 'Knight B.png'))
white_knight = pygame.image.load(os.path.join('Chess Pieces', 'Knight W.png'))
black_bishop = pygame.image.load(os.path.join('Chess Pieces', 'Bishop B.png'))
white_bishop = pygame.image.load(os.path.join('Chess Pieces', 'Bishop W.png'))
black_queen = pygame.image.load(os.path.join('Chess Pieces', 'Queen B.png'))
white_queen = pygame.image.load(os.path.join('Chess Pieces', 'Queen W.png'))
black_rook = pygame.image.load(os.path.join('Chess Pieces', 'Rook B.png'))
white_rook = pygame.image.load(os.path.join('Chess Pieces', 'Rook W.png'))