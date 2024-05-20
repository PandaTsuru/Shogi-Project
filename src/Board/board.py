import pygame
from constants import TILE_SIZE, HEIGHT, WIDTH, selected_asset
from Board.tile import Tile
from Board.pieces import *
from utils import notation_to_piece, generate_piece_images, draw_text, load_image

class Board:
    def __init__(self, size):
        self.tile_image = load_image('assets/boards/tile_wood1.png', (TILE_SIZE, TILE_SIZE))
        self.size = size
        self.selected_piece = None
        self.current_player = -1
        self.winner = None
        self.piece_images = generate_piece_images(selected_asset, TILE_SIZE)
        self.reserves = {player: {piece: [] for piece in 'PLNSGBR'} for player in (-1, 1)}
        self.create_board()

    def create_board(self):
        config = 'LNSGKGSNL/0B00000R0/PPPPPPPPP/000000000/000000000/000000000/PPPPPPPPP/0R00000B0/LNSGKGSNL'
        self.board = [[Tile(i, j) for j in range(9)] for i in range(9)]
        for i, row in enumerate(config.split('/')):
            for j, char in enumerate(row):
                if char != '0':
                    player = 1 if i < 3 else -1
                    self.board[i][j].occupying_piece = notation_to_piece(char)(i, j, player)

    def select(self, row: int, column: int):
        self.selected_piece = None
        if 0 <= row < 9 and 0 <= column < 9:
            piece = self.get_piece(row, column)
            if piece and piece.player == self.current_player:
                self.selected_piece = piece
                self.selected_piece.get_moves(row, column, self)
        elif self.is_valid_reserve_selection(row, column):
            self.selected_piece = self.get_piece_from_reserve(column)

    def is_valid_reserve_selection(self, row, column):
        return ((row == -1 and 1 <= column < 8 and self.current_player == 1) or
                (row == 9 and 1 <= column < 8 and self.current_player == -1))

    def get_piece_from_reserve(self, column):
        piece_type = list(self.reserves[self.current_player].keys())[column - 1]
        if self.reserves[self.current_player][piece_type]:
            piece = self.reserves[self.current_player][piece_type][0]
            piece.moves = self.get_empty_tiles()
            return piece
        return None

    def make_move(self, move):
        capture = self.get_piece(*move)
        self.move_piece(self.selected_piece, move)
        if capture:
            self.capture_piece(capture)
        if isinstance(self.selected_piece, (Pawn, Knight, Lance, Silver, Rook, Bishop)) and (self.selected_piece.row <= 2 and self.current_player == -1 or self.selected_piece.row >= 6 and self.current_player == 1) and not self.selected_piece.promoted:
            self.selected_piece.promote()
        self.change_turn()

    def make_drop(self, move):
        self.place_piece(self.selected_piece, move)
        self.change_turn()

    def move_piece(self, piece, move):
        self.board[piece.row][piece.column].occupying_piece = None
        self.board[move[0]][move[1]].occupying_piece = piece
        piece.move(*move)

    def capture_piece(self, piece):
        if piece.notation != 'K':
            piece.__init__(None, None, self.current_player)
            self.reserves[self.current_player][piece.notation].append(piece)
        else :
            self.winner = self.current_player
            print(f'{'black' if self.winner == 1 else 'white'} win')

    def place_piece(self, piece, move):
        self.board[move[0]][move[1]].occupying_piece = piece
        piece.move(*move)
        self.remove_piece_from_reserve(piece)
        self.selected_piece = None

    def remove_piece_from_reserve(self, piece):
        self.reserves[self.current_player][piece.notation].remove(piece)

    def change_turn(self):
        self.selected_piece = None
        self.current_player *= -1

    def get_piece(self, row, column):
        return self.board[row][column].occupying_piece

    def get_empty_tiles(self):
        return [(tile.row, tile.column) for row in self.board for tile in row if not tile.occupying_piece]

    def handle_left_click(self):
        x, y = pygame.mouse.get_pos()
        row, column = int((y - HEIGHT * 0.1) // TILE_SIZE), int(x // TILE_SIZE)
        if self.selected_piece and (row, column) in self.selected_piece.moves:
            if self.selected_piece.row is not None:
                self.make_move((row, column))
            else:
                self.make_drop((row, column))
        else:
            self.select(row, column)

    def draw(self, screen):
        self.draw_tiles(screen)
        self.draw_pieces(screen)
        if self.selected_piece:
            self.draw_moves(screen)
        self.draw_reserves(screen)

    def draw_tiles(self, screen):
        for i in range(11):
            for j in range(9):
                screen.blit(self.tile_image, (j * TILE_SIZE, i * TILE_SIZE))
                if 0 < i < 10:
                    self.board[i - 1][j].draw(screen)
        pygame.draw.rect(screen, 'black', (0, TILE_SIZE, TILE_SIZE * 9, TILE_SIZE * 9), 2)

    def draw_pieces(self, screen):
        for row in self.board:
            for tile in row:
                if tile.occupying_piece:
                    screen.blit(tile.occupying_piece.image, (tile.x, tile.y))

    def draw_moves(self, screen):
        for move in self.selected_piece.moves:
            pygame.draw.circle(screen, 'grey', (move[1] * TILE_SIZE + TILE_SIZE // 2, move[0] * TILE_SIZE + TILE_SIZE // 2 + TILE_SIZE), TILE_SIZE // 8)

    def draw_reserves(self, screen):
        for i, notation in enumerate('PLNSGBR'):
            self.draw_reserve_piece(screen, notation, i, 1)
            if len(self.reserves[1][notation]) > 1:
                draw_text(screen, str(len(self.reserves[1][notation])), pygame.font.Font(None, TILE_SIZE // 2), 'black', (TILE_SIZE + TILE_SIZE * i, 0))
            self.draw_reserve_piece(screen, notation, i, -1)
            if len(self.reserves[-1][notation]) > 1:
                draw_text(screen, str(len(self.reserves[-1][notation])), pygame.font.Font(None, TILE_SIZE // 2), 'black', (TILE_SIZE + TILE_SIZE * i, HEIGHT - TILE_SIZE))

    def draw_reserve_piece(self, screen, notation, i, position):
        y_pos = 0 if position == 1 else HEIGHT - TILE_SIZE
        image = self.piece_images[position][notation]
        image.set_alpha(255 if self.reserves[position][notation] else 100)
        screen.blit(image, (TILE_SIZE + TILE_SIZE * i, y_pos))
