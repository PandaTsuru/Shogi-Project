import pygame
import os
from src.constants import selected_asset, TILE_SIZE

class Piece:
    def __init__(self, row:int, column:int, player:str, notation:str):
        self.row = row
        self.column = column
        self.player = player
        self.notation = notation
        self.moves = []
        self.image = pygame.transform.scale(pygame.image.load(os.path.join('assets', selected_asset, f'{notation}.png')), (TILE_SIZE, TILE_SIZE)) if player == -1 else pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join('assets', selected_asset, f'{notation}.png')), (TILE_SIZE, TILE_SIZE)), 180)

    def move(self, row, column):
        self.row = row
        self.column = column

    def get_moves(self, row, column, board):
        pass

class Pawn(Piece):
    def __init__(self, row, column, player):
        super().__init__(row, column, player, 'P')

class Bishop(Piece):
    def __init__(self, row, column, player):
        super().__init__(row, column, player, 'B')

class Rook(Piece):
    def __init__(self, row, column, player):
        super().__init__(row, column, player, 'R')

class Knight(Piece):
    def __init__(self, row, column, player):
        super().__init__(row, column, player, 'N')

class Gold(Piece):
        def __init__(self, row, column, player):
            super().__init__(row, column, player, 'G')
        
class Silver(Piece):
    def __init__(self, row, column, player):
        super().__init__(row, column, player, 'S')

class Lance(Piece):
    def __init__(self, row, column, player):
        super().__init__(row, column, player, 'L')

class King(Piece):
    def __init__(self, row, column, player):
        super().__init__(row, column, player, 'K')























