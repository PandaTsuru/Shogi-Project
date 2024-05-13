import pygame
from src.scene import Scene, SceneManager
from src.config import Config
from src.board import Board

class Game(Scene):
    def __init__(self, manager:SceneManager, config:Config):
        super().__init__(manager, config)
        self.winner = None
        self.board = Board()

    def render(self, screen:pygame.Surface):
        pass

    def update(self):
        pass

    def handle_event(self, event:pygame.event.Event):
        pass

        
    
