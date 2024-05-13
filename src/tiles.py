from src.constants import TILE_SIZE
import pygame

class Tile:
    def __init__(self, x, y, image):
        self.image = image
        self.x = x
        self.y = y
        self.abs_x = x*TILE_SIZE
        self.abs_y = y*TILE_SIZE
        self.occupying_piece = None
        self.highlight_color = None

    def get_position(self):
        return (9-self.x, self.y+1)
    
    def draw(self, screen):
        screen.blit(self.image, (self.abs_x, self.abs_y))
        pygame.draw.rect(screen, 'black', (self.abs_x, self.abs_y, TILE_SIZE, TILE_SIZE), 1)

