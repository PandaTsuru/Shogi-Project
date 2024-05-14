import pygame
from src.scene import Scene, SceneManager
from config import Config
from board import Board

class Game(Scene):
    def __init__(self, manager:SceneManager, config:Config):
        super().__init__(manager, config)
        self.winner = None
        self.board = Board()

    def render(self, screen:pygame.Surface):
        self.board.draw_tiles(screen)

    def update(self):
        pass

    def handle_event(self, event:pygame.event.Event):
        pass

        
    
