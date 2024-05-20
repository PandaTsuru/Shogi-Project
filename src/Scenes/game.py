import pygame
from Scenes.scene import Scene, SceneManager
from config import Config
from Board.board import Board
from constants import TILE_SIZE, HEIGHT

class Game(Scene):
    def __init__(self, manager:SceneManager, config:Config):
        super().__init__(manager, config)
        self.board = Board(9)


    def render(self, screen:pygame.Surface):
        self.board.draw(screen)


    def update(self):
        pass


    def handle_event(self, event:pygame.event.Event):
        if event.type == pygame.MOUSEBUTTONDOWN :
            if pygame.mouse.get_pressed()[0]:
                self.board.handle_left_click()

        
    
