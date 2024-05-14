import pygame
from src.scene import Scene, SceneManager
from src.config import Config
from src.board import Board
from src.constants import TILE_SIZE

class Game(Scene):
    def __init__(self, manager:SceneManager, config:Config):
        super().__init__(manager, config)
        self.winner = None
        self.board = Board()
        self.selected_piece = None

    def select(self, row:int, column:int):
        self.selected_piece = self.board.get_piece(row, column)
        self.selected_piece.get_moves(row, column, self.board.board)

    def make_move(self, move):
        self.board.move_piece(self.selected_piece, move)
        self.selected_piece = None

    def render(self, screen:pygame.Surface):
        self.board.draw_tiles(screen)
        self.board.draw_pieces(screen)
        if self.selected_piece :
            self.board.draw_moves(screen, self.selected_piece.moves)

    def update(self):
        pass

    def handle_left_clik(self):
        x, y = pygame.mouse.get_pos()
        row, column = int(y//TILE_SIZE), int(x//TILE_SIZE)

        if self.selected_piece and (row, column) in self.selected_piece.moves :
            self.make_move((row, column))
        elif self.board.get_piece(row, column):
            self.select(row, column)
        else :
            self.selected_piece = None
        
        
    def handle_event(self, event:pygame.event.Event):
        if event.type == pygame.MOUSEBUTTONDOWN :
            if pygame.mouse.get_pressed()[0]:
                self.handle_left_clik()

        
    
