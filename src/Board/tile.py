from constants import TILE_SIZE, HEIGHT, MARGIN
import pygame

class Tile:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.x = column*TILE_SIZE + MARGIN
        self.y = row*TILE_SIZE + TILE_SIZE + MARGIN
        self.occupying_piece = None
        self.highlight_color = None

    def get_position(self):
        return (9-self.x, self.y+1)
    
    def draw(self, screen):
        pygame.draw.rect(screen, 'black', (self.x, self.y, TILE_SIZE, TILE_SIZE), 1)

