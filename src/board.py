import pygame
from src.constants import TILE_SIZE
from src.tile import Tile
from src.pieces import *
from src.utils import notation_to_piece

class Board:
    def __init__(self):
        self.tile_image = pygame.transform.scale(pygame.image.load('assets/boards/tile_wood1.png'), (TILE_SIZE, TILE_SIZE))
        self.create_board()

    def create_board(self):
        config = 'LNSGKGSNL/0B00000R0/PPPPPPPPP/000000000/000000000/000000000/PPPPPPPPP/0P00000B0/LNSGKGSNL'
        self.board = [[Tile(i, j, self.tile_image) for j in range(9)] for i in range(9)]
        for i, row in enumerate(config.split('/')):
            for j, char in enumerate(row):
                if char != '0':
                    self.board[i][j].occupying_piece = notation_to_piece(char)(i, j, 1 if i < 3 else -1)


    def draw_tiles(self, screen):
        for row in self.board :
            for tile in row :
                tile.draw(screen)

    def draw_pieces(self, screen):
        for row in self.board :
            for tile in row :
                if tile.occupying_piece :
                    screen.blit(tile.occupying_piece.image, (tile.x, tile.y))
