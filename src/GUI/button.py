import pygame
from GUI.text import Label

class Button(pygame.sprite.Sprite):
    def __init__(self, center:tuple[int, int], image:pygame.Surface, command):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.command = command
    
    def handle_click(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.command




    