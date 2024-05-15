import pygame
from constants import TILE_SIZE
from Board.tile import Tile
from Board.pieces import *
from utils import notation_to_piece

class Board:
    def __init__(self, size):
        self.tile_image = pygame.transform.scale(pygame.image.load('assets/boards/tile_wood1.png'), (TILE_SIZE, TILE_SIZE))
        self.size = size
        self.create_board()

    def create_board(self):
        config = 'LNSGKGSNL/0B00000R0/PPPPPPPPP/000000000/000000000/000000000/PPPPPPPPP/0R00000B0/LNSGKGSNL'
        self.board = [[Tile(i, j, self.tile_image) for j in range(9)] for i in range(9)]
        for i, row in enumerate(config.split('/')):
            for j, char in enumerate(row):
                if char != '0':
                    self.board[i][j].occupying_piece = notation_to_piece(char)(i, j, 1 if i < 3 else -1)

    def get_piece(self, row, column):
        return self.board[row][column].occupying_piece
    
    def move_piece(self, piece, move):
        self.board[piece.row][piece.column].occupying_piece = None
        self.board[move[0]][move[1]].occupying_piece = piece
        piece.move(move[0], move[1])
    
    def draw_tiles(self, screen):
        for row in self.board :
            for tile in row :
                tile.draw(screen)

    def draw_pieces(self, screen):
        for row in self.board :
            for tile in row :
                if tile.occupying_piece :
                    screen.blit(tile.occupying_piece.image, (tile.x, tile.y))
    
    def draw_moves(self, screen, moves):
        for move in moves :
            pygame.draw.circle(screen, 'grey', (move[1]*TILE_SIZE+TILE_SIZE//2, move[0]*TILE_SIZE+TILE_SIZE//2), TILE_SIZE//6)

            
