import pygame
from src.constants import TILE_SIZE
from src.tiles import Tile
from src.pieces import *
from src.utils import notation_to_piece

class Board:
    def __init__(self):
        self.tile_image = pygame.transform.scale(pygame.image.load('assets/boards/tile_wood1.png'), (TILE_SIZE, TILE_SIZE))
        self.create_board()

    def create_board(self):

        config = 'LNSGKGSNL/00B000R00/PPPPPPPPP/000000000/000000000/000000000/PPPPPPPPP/00P000B00/LNSGKGSNL'
        self.board = [[Tile(i, j, self.tile_image) for j in range(9)] for i in range(9)]
        for i, row in enumerate(config.split('/')):
            for j, char in enumerate(row):
                if char != '0':
                    self.board[i][j].occupying_piece = notation_to_piece(char)()
                print(self.board[i][j].occupying_piece)




    def draw_tiles(self, screen):
        for row in self.board :
            for tile in row :
                tile.draw(screen)
