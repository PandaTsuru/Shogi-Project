from constants import TILE_SIZE
import pygame

class Tile:
    def __init__(self, row, column, image):
        self.image = image
        self.row = row
        self.column = column
        self.x = column*TILE_SIZE
        self.y = row*TILE_SIZE
        self.occupying_piece = None
        self.highlight_color = None

    def get_position(self):
        return (9-self.x, self.y+1)
    
    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
        pygame.draw.rect(screen, 'black', (self.x, self.y, TILE_SIZE, TILE_SIZE), 1)

