import pygame

class Piece:
    def __init__(self, row:int, column:int, player:str):
        self.row = row
        self.column = column
        self.player = player
        self.moves = []

    def move(self, row, column):
        self.row = row
        self.column = column




